# HHRU

Курсовая работа по созданию системы получения данных о компаниях и вакансиях с сайта hh.ru на Python, реализованная в
рамках курса «Python-разработчик с нуля» от онлайн-университета Skypro.

---

## Структура проекта

```
hhru/
├── data/
│   ├── hh_vacancies.json
├── htmlcov/
├── src/
│   ├── __init__.py
│   ├── abstact.py
│   ├── hh_api.py
│   ├── hh_file.py
│   └── vacancy.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_hh_api.py
│   ├── test_hh_file.py
│   └── test_vacancy.py
├── .coverage
├── flake8
├── .gitignore
├── coverage.txt
├── lint.sh
├── main.py
├── poetry.loc
├── pyproject.toml
└── README.MD
```

---

## Установка

Клонировать репозиторий и установить зависимости через `poetry`:

```bash
# Клонировать проект
git clone git@github.com:ivanitch/hhru.git hhru
cd hhru

# Установить зависимости
poetry install

# Отдельно ставим группы (тесты, покрытие, линтеры)
poetry install --with dev,lint
```

---

## Запуск приложения

```shell
poetry run python main.py
```

Пример работы:
```
Вакансия: ML инженер в Yandex (ЗП: 100307 - 237024)
Вакансия: Python разработчик в Ozon Tech (ЗП: 123188 - 312644)
Вакансия: Python разработчик в Sber (ЗП: 145410 - 397162)
Вакансия: Data Engineer в Yandex (ЗП: 194125 - 256468)
Вакансия: Python разработчик в Sber (ЗП: 186403 - 308172)
Вакансия: Python разработчик в Yandex (ЗП: 188976 - 215637)
Вакансия: Python разработчик в Sber (ЗП: 190527 - 262644)
Вакансия: Python разработчик в Tinkoff (ЗП: 176092 - 355364)
Вакансия: Python разработчик в Ozon Tech (ЗП: 160113 - 383316)
Вакансия: Data Engineer в Tinkoff (ЗП: 137142 - 348015)
Вакансия: Backend инженер в Sber (ЗП: 167943 - 303641)
Вакансия: Python разработчик в VK (ЗП: 189079 - 397664)
Вакансия: ML инженер в VK (ЗП: 102559 - 359502)
Вакансия: Python разработчик в VK (ЗП: 186460 - 208218)
Вакансия: Backend инженер в Tinkoff (ЗП: 152327 - 266907)
Вакансия: ML инженер в Tinkoff (ЗП: 103688 - 284925)
Вакансия: ML инженер в Yandex (ЗП: 183481 - 344146)
Вакансия: Python разработчик в Ozon Tech (ЗП: 145478 - 223063)
Вакансия: Python разработчик в Ozon Tech (ЗП: 150259 - 246410)
Вакансия: Data Engineer в VK (ЗП: 110245 - 397940)
Вакансия: Python разработчик в VK (ЗП: 144380 - 208989)
Вакансия: Backend инженер в Tinkoff (ЗП: 116542 - 339685)
Вакансия: Backend инженер в Ozon Tech (ЗП: 152007 - 297880)
Вакансия: ML инженер в Tinkoff (ЗП: 126320 - 276015)
Вакансия: Python разработчик в Sber (ЗП: 103786 - 365522)
```

---

## Запуск тестов

```bash
# Запуск всех тестов
poetry run pytest

# Подробный вывод
poetry run pytest -v

# С отчётом о покрытии кода
poetry run pytest tests -v --cov=src --cov-report=html

# Сразу показывает непротестированные строки в консоли
poetry run pytest tests --cov=src --cov-report=term-missing --cov-report=html
```

### Просмотр покрытия

```bash
poetry run coverage report                 # таблица в консоли
poetry run coverage report > coverage.txt  # направить отчёт в файл `coverage.txt`
poetry run coverage html                   # HTML-отчёт в папке htmlcov/ с интерактивным сайтом (htmlcov/index.html)
```

Файл `coverage.txt`:

```bash
Name              Stmts   Miss  Cover
-------------------------------------
src/__init__.py       0      0   100%
src/abstact.py        5      1    80%
src/hh_api.py        23      0   100%
src/hh_file.py        9      0   100%
src/vacancy.py       26      1    96%
-------------------------------------
TOTAL                63      2    97%
```

---

## Кодстайл

```bash
poetry run flake8 src tests          # линтер
poetry run black src tests           # форматирование
poetry run isort src tests           # сортировка импортов
poetry run mypy src                  # проверка типов
```

Или запустить все линтеры одной командой:

```bash
poetry run lint.sh
```
