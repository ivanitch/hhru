from unittest.mock import MagicMock, patch
from src.hh_api import HHApi


@patch("src.hh_api.requests.get")
def test_get_company(mock_get: MagicMock) -> None:
    mock_get.return_value.json.return_value = {"id": "1740", "name": "Яндекс"}
    mock_get.return_value.raise_for_status = MagicMock()

    api = HHApi(employer_ids=[1740])
    result = api.get_company(1740)

    assert result["name"] == "Яндекс"
    mock_get.assert_called_once()


@patch("src.hh_api.requests.get")
def test_get_vacancies(mock_get: MagicMock) -> None:
    mock_get.return_value.json.return_value = {
        "items": [
            {"name": "Python разработчик", "employer": {"name": "Яндекс"}}
        ]
    }
    mock_get.return_value.raise_for_status = MagicMock()

    api = HHApi(employer_ids=[1740])
    result = api.get_vacancies(1740)

    assert len(result) == 1
    assert result[0]["name"] == "Python разработчик"


@patch("src.hh_api.requests.get")
def test_get_all_vacancies(mock_get: MagicMock) -> None:
    mock_get.return_value.json.return_value = {
        "items": [{"name": "Python разработчик"}]
    }
    mock_get.return_value.raise_for_status = MagicMock()

    api = HHApi(employer_ids=[1740, 3529])
    result = api.get_all_vacancies()

    assert len(result) == 2  # по одной вакансии от каждой компании
    assert mock_get.call_count == 2
