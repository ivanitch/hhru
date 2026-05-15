import requests

from src.abstact import AbstarctAPI


class HHApi(AbstarctAPI):
    """Класс для получения данных с hh.ru через публичный API."""

    BASE_URL = "https://api.hh.ru"

    def __init__(self, employer_ids: list[int]) -> None:
        self.employer_ids = employer_ids
        self.headers = {"User-Agent": "hhru-project/1.0"}

    def get_company(self, employer_id: int) -> dict:
        """Получить данные компании по id."""
        url = f"{self.BASE_URL}/employers/{employer_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, employer_id: int) -> list[dict]:
        """Получить список вакансий компании."""
        url = f"{self.BASE_URL}/vacancies"
        params = {"employer_id": employer_id, "per_page": 100}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json().get("items", [])

    def get_all_vacancies(self) -> list[dict]:
        """Получить вакансии всех компаний из списка."""
        vacancies = []
        for employer_id in self.employer_ids:
            vacancies.extend(self.get_vacancies(employer_id))
        return vacancies
