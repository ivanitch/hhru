from src.abstact import AbstarctAPI
import json


class HHFile(AbstarctAPI):

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def get_all_vacancies(self) -> list[dict]:
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data.get("items", [])
