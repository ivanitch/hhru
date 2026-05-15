import json
from unittest.mock import mock_open, patch

from src.hh_file import HHFile

FAKE_DATA = {
    "items": [
        {
            "name": "Python разработчик",
            "employer": {"name": "Яндекс"},
            "salary": {"from": 100000, "to": 200000},
            "alternate_url": "https://hh.ru/vacancy/123",
        }
    ]
}


@patch("builtins.open", mock_open(read_data=json.dumps(FAKE_DATA)))
def test_hh_file_get_all_vacancies() -> None:
    api = HHFile(file_path="any_path.json")
    result = api.get_all_vacancies()

    assert len(result) == 1
    assert result[0]["name"] == "Python разработчик"


@patch("builtins.open", mock_open(read_data=json.dumps({})))
def test_hh_file_returns_empty_if_no_items() -> None:
    api = HHFile(file_path="any_path.json")
    result = api.get_all_vacancies()

    assert result == []
