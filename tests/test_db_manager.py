from unittest.mock import ANY, MagicMock, patch

import pytest

from src.db_manager import DBManager


@pytest.fixture
def db() -> DBManager:
    with patch("src.db_manager.psycopg.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        instance = DBManager()
        yield instance


def test_get_companies_and_vacancies_count(db: DBManager) -> None:
    mock_cursor = db._conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchall.return_value = [("Yandex", 5), ("Sber", 3)]

    result = db.get_companies_and_vacancies_count()

    assert len(result) == 2
    assert result[0] == ("Yandex", 5)
    mock_cursor.execute.assert_called_once()


def test_get_all_vacancies(db: DBManager) -> None:
    mock_cursor = db._conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchall.return_value = [
        ("Yandex", "Python разработчик", 100000, 200000, "https://hh.ru/vacancy/1")
    ]

    result = db.get_all_vacancies()

    assert len(result) == 1
    assert result[0][1] == "Python разработчик"
    mock_cursor.execute.assert_called_once()


def test_get_avg_salary(db: DBManager) -> None:
    mock_cursor = db._conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchone.return_value = (150000.0,)

    result = db.get_avg_salary()

    assert result == 150000.0
    mock_cursor.execute.assert_called_once()


def test_get_avg_salary_no_data(db: DBManager) -> None:
    mock_cursor = db._conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchone.return_value = (None,)

    result = db.get_avg_salary()

    assert result == 0.0


def test_get_vacancies_with_higher_salary(db: DBManager) -> None:
    mock_cursor = db._conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchall.return_value = [
        ("Yandex", "Data Engineer", 200000, 300000, "https://hh.ru/vacancy/2")
    ]

    result = db.get_vacancies_with_higher_salary()

    assert len(result) == 1
    assert result[0][2] == 200000
    mock_cursor.execute.assert_called_once()


def test_get_vacancies_with_keyword(db: DBManager) -> None:
    mock_cursor = db._conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchall.return_value = [
        ("Sber", "Python разработчик", 150000, 250000, "https://hh.ru/vacancy/3")
    ]

    result = db.get_vacancies_with_keyword("python")

    assert len(result) == 1
    assert "Python" in result[0][1]
    mock_cursor.execute.assert_called_once_with(ANY, ("%python%",))
