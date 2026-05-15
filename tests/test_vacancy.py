from src.vacancy import Vacancy


def test_init(vacancy_factory):
    vacancy = vacancy_factory()
    assert vacancy.name == "Python разработчик"
    assert vacancy.company == "Yandex"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 200000
    assert vacancy.url == "https://hh.ru/vacancy/123"


def test_vacancy_str_with_salary(vacancy_factory):
    vacancy = vacancy_factory(salary_from=100000, salary_to=200000)
    assert "100000" in str(vacancy)


def test_vacancy_str_none_salary(vacancy_factory):
    vacancy = vacancy_factory(salary_from=None, salary_to=None)
    assert "не указана" in str(vacancy)


def test_vacancy_lt(vacancy_factory):
    v1 = vacancy_factory()
    v2 = vacancy_factory(salary_from=150000)
    assert v1 < v2


def test_vacancy_lt_none_salary(vacancy_factory):
    v_no_salary = vacancy_factory(salary_from=None, salary_to=None)
    v_with_salary = vacancy_factory(salary_from=50000)
    assert v_no_salary < v_with_salary


def test_vacancy_str_only_from(vacancy_factory):
    vacancy = vacancy_factory(salary_from=100000, salary_to=None)
    assert "от 100000" in str(vacancy)


def test_vacancy_str_only_to(vacancy_factory):
    vacancy = vacancy_factory(salary_from=None, salary_to=200000)
    assert "до 200000" in str(vacancy)


def test_vacancy_from_dict(vacancy_factory):
    data = {
        "name": "ML инженер",
        "employer": {"name": "Yandex"},
        "salary": {"from": 100000, "to": 200000},
        "alternate_url": "https://hh.ru/vacancy/123",
    }
    vacancy = Vacancy.from_dict(data)
    expected = vacancy_factory(name="ML инженер")
    assert vacancy.name == expected.name
    assert vacancy.company == expected.company
    assert vacancy.salary_from == expected.salary_from
