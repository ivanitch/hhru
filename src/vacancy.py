from __future__ import annotations


class Vacancy:
    """Класс вакансии."""

    def __init__(
        self, name: str, company: str, salary_from: int | None, salary_to: int | None, url: str | None
    ) -> None:
        self.name = name
        self.company = company
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url

    def __str__(self) -> str:
        if self.salary_from and self.salary_to:
            salary_str = f"{self.salary_from} - {self.salary_to}"
        elif self.salary_from:
            salary_str = f"от {self.salary_from}"
        elif self.salary_to:
            salary_str = f"до {self.salary_to}"
        else:
            salary_str = "не указана"
        return f"Вакансия: {self.name} в {self.company} (ЗП: {salary_str})"

    def __repr__(self) -> str:
        return (
            f"Vacancy(name={self.name!r},"
            f" company={self.company!r},"
            f" salary_from={self.salary_from},"
            f" salary_to={self.salary_to}), "
            f" url={self.url!r})"
        )

    def __lt__(self, other: Vacancy) -> bool:
        """Сравнение по зп (сортировка)."""
        return (self.salary_from or 0) < (other.salary_from or 0)

    @classmethod
    def from_dict(cls, data: dict) -> Vacancy:
        """Создать вакансию из словаря."""
        employer_data = data.get("employer") or {}
        salary_data = data.get("salary") or {}

        return cls(
            name=data.get("name"),
            company=employer_data.get("name"),
            salary_from=salary_data.get("from"),
            salary_to=salary_data.get("to"),
            url=data.get("alternate_url"),
        )
