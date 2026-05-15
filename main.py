from src.vacancy import Vacancy

if __name__ == '__main__':
    vacancy = Vacancy(
        "Разработчик Python",
        "Google",
        300_000,
        500_000,
        "https://link.com)"
    )

    print(vacancy)
