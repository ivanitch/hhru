from src.hh_api import HHApi
from src.hh_file import HHFile
from src.vacancy import Vacancy


def main() -> None:
    # employer_ids = [1740, 3529, 78638]  # Яндекс, Сбер, Тинькофф
    #
    # api = HHApi(employer_ids=employer_ids)
    # raw_vacancies = api.get_all_vacancies()
    #
    # vacancies = [Vacancy.from_dict(v) for v in raw_vacancies]
    #
    # for vacancy in vacancies:
    #     print(vacancy)

    api = HHFile(file_path="data/hh_vacancies.json")
    raw_vacancies = api.get_all_vacancies()
    vacancies = [Vacancy.from_dict(v) for v in raw_vacancies]

    for vacancy in vacancies:
        print(vacancy)


if __name__ == "__main__":
    main()
