# HHRU

Курсовая работа по созданию системы получения данных о компаниях и вакансиях с сайта hh.ru на Python, реализованная в
рамках курса «Python-разработчик с нуля» от онлайн-университета Skypro.

---

## Структура проекта

```
hhru/
├── data/
│   ├── db/
│   ├──── create_db.sql
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
├── .env.example
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

## База данных

Скопировать файл `.env.example` в `.env` настроить подключение к БД.

```bash
cp .env.example .env
````

---

## Запуск приложения

```shell
poetry run python main.py
```

Пример работы:
```
2026-05-16T13:10:58 | INFO     | src.db_manager | Подключение к БД установлено
2026-05-16T13:10:58 | INFO     | src.db_manager | Таблицы созданы
2026-05-16T13:10:58 | INFO     | src.db_manager | Данные загружены: 5 компаний, 25 вакансий

Выберите действие:
1. Компании и количество вакансий
2. Все вакансии
3. Средняя зарплата
4. Вакансии выше средней зарплаты
5. Поиск вакансий по ключевому слову
0. Выход

Ваш выбор:
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
Name                Stmts   Miss  Cover
---------------------------------------
src/__init__.py         0      0   100%
src/abstact.py          5      1    80%
src/db_manager.py      52     16    69%
src/exceptions.py       6      0   100%
src/hh_api.py          23      0   100%
src/hh_file.py          9      0   100%
src/logger.py           9      0   100%
src/vacancy.py         26      1    96%
---------------------------------------
TOTAL                 130     18    86%
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
poetry run ./lint.sh
```
