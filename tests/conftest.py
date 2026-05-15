import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_factory():
    """Фабрика вакансий."""

    def factory(**kwargs) -> Vacancy:
        data = {
            "name": "Python разработчик",
            "company": "Yandex",
            "salary_from": 100000,
            "salary_to": 200000,
            "url": "https://hh.ru/vacancy/123",
        }

        data.update(kwargs)
        return Vacancy(**data)

    return factory
