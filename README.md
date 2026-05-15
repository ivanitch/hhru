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
src/hh_file.py        9      9     0%
src/vacancy.py       26      1    96%
-------------------------------------
TOTAL                63     11    83%
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
