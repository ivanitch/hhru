from src.db_manager import DBManager
from src.hh_file import HHFile
from src.logger import setup_logger
import json

logger = setup_logger(__name__)


def main() -> None:
    api = HHFile(file_path="data/hh_vacancies.json")
    companies = json.load(open("data/companies.json"))

    db = DBManager()
    db.create_tables()
    db.fill_data(companies, api.get_all_vacancies())

    while True:
        print("\nВыберите действие:")
        print("1. Компании и количество вакансий")
        print("2. Все вакансии")
        print("3. Средняя зарплата")
        print("4. Вакансии выше средней зарплаты")
        print("5. Поиск вакансий по ключевому слову")
        print("0. Выход")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            for row in db.get_companies_and_vacancies_count():
                print(f"{row[0]}: {row[1]} вакансий")
        elif choice == "2":
            for row in db.get_all_vacancies():
                print(f"{row[0]} | {row[1]} | от {row[2]} до {row[3]} | {row[4]}")
        elif choice == "3":
            print(f"Средняя зарплата: {db.get_avg_salary()} руб.")
        elif choice == "4":
            for row in db.get_vacancies_with_higher_salary():
                print(f"{row[0]} | {row[1]} | от {row[2]} до {row[3]} | {row[4]}")
        elif choice == "5":
            keyword = input("Введите ключевое слово: ").strip()
            results = db.get_vacancies_with_keyword(keyword)
            if results:
                for row in results:
                    print(f"{row[0]} | {row[1]} | от {row[2]} до {row[3]} | {row[4]}")
            else:
                print("Вакансий не найдено")
        elif choice == "0":
            db.close()
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
