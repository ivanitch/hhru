from abc import ABC, abstractmethod


class AbstarctAPI(ABC):
    @abstractmethod
    def get_all_vacancies(self) -> list[dict]:
        pass
