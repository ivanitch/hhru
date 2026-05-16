class HHRuError(Exception):
    """Базовое исключение проекта."""
    pass


class DBConnectionError(HHRuError):
    """Ошибка подключения к БД."""
    pass


class APIError(HHRuError):
    """Ошибка запроса к API."""
    pass
