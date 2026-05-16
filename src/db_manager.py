import psycopg
from dotenv import load_dotenv
import os

from src.exceptions import DBConnectionError
from src.logger import setup_logger

load_dotenv()
logger = setup_logger(__name__)


class DBManager:
    """Класс для работы с БД PostgreSQL."""

    def __init__(self) -> None:
        try:
            self._conn = psycopg.connect(
                host=os.getenv("DB_HOST", "localhost"),
                port=os.getenv("DB_PORT", "5432"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
            )
            logger.info("Подключение к БД установлено")
        except Exception as e:
            logger.exception("Ошибка подключения к БД")
            raise DBConnectionError(str(e))

    def create_tables(self) -> None:
        """Создать таблицы если не существуют."""
        with self._conn.cursor() as cur:
            cur.execute(open("data/db/create_db.sql").read())
        self._conn.commit()
        logger.info("Таблицы созданы")

    def fill_data(self, companies: list[dict], vacancies: list[dict]) -> None:
        """Заполнить таблицы данными."""
        with self._conn.cursor() as cur:
            for company in companies:
                cur.execute(
                    "INSERT INTO companies (company_id, company_name) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                    (company["id"], company["name"]),
                )
            for vacancy in vacancies:
                cur.execute(
                    "INSERT INTO vacancies (vacancy_id, company_id, vacancy_name, salary_from, salary_to, url) "
                    "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;",
                    (
                        vacancy["id"],
                        vacancy["employer"]["id"],
                        vacancy["name"],
                        vacancy.get("salary", {}) and vacancy["salary"].get("from"),
                        vacancy.get("salary", {}) and vacancy["salary"].get("to"),
                        vacancy["alternate_url"],
                    ),
                )
        self._conn.commit()
        logger.info("Данные загружены: %s компаний, %s вакансий", len(companies), len(vacancies))

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        with self._conn.cursor() as cur:
            cur.execute(
                "SELECT companies.company_name, COUNT(vacancies.vacancy_id) "
                "FROM companies "
                "LEFT JOIN vacancies USING(company_id) "
                "GROUP BY companies.company_name;"
            )
            return cur.fetchall()

    def get_all_vacancies(self) -> list[tuple]:
        """Список всех вакансий с названием компании, вакансии, зарплатой и ссылкой."""
        with self._conn.cursor() as cur:
            cur.execute("""
                SELECT c.company_name, v.vacancy_name, v.salary_from, v.salary_to, v.url
                FROM vacancies v
                JOIN companies c USING(company_id)
                ORDER BY v.salary_from DESC NULLS LAST;
            """)
            return cur.fetchall()

    def get_avg_salary(self) -> float:
        """Средняя зарплата по всем вакансиям."""
        with self._conn.cursor() as cur:
            cur.execute("""
                SELECT ROUND(AVG(salary_from)::numeric, 2)
                FROM vacancies
                WHERE salary_from IS NOT NULL;
            """)
            result = cur.fetchone()
            return float(result[0]) if result and result[0] else 0.0

    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        """Вакансии с зарплатой выше средней."""
        with self._conn.cursor() as cur:
            cur.execute("""
                SELECT c.company_name, v.vacancy_name, v.salary_from, v.salary_to, v.url
                FROM vacancies v
                JOIN companies c USING(company_id)
                WHERE v.salary_from > (
                    SELECT AVG(salary_from)
                    FROM vacancies
                    WHERE salary_from IS NOT NULL
                )
                ORDER BY v.salary_from DESC;
            """)
            return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword: str) -> list[tuple]:
        """Вакансии у которых в названии содержится ключевое слово."""
        with self._conn.cursor() as cur:
            cur.execute("""
                SELECT c.company_name, v.vacancy_name, v.salary_from, v.salary_to, v.url
                FROM vacancies v
                JOIN companies c USING(company_id)
                WHERE v.vacancy_name ILIKE %s
                ORDER BY v.salary_from DESC NULLS LAST;
            """, (f"%{keyword}%",))
            return cur.fetchall()

    def close(self) -> None:
        """Закрыть соединение с БД."""
        self._conn.close()
        logger.info("Соединение с БД закрыто")
