-- CREATE DATABASE hhru OWNER postgres;

CREATE TABLE IF NOT EXISTS companies (
    company_id   INTEGER PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS vacancies (
    vacancy_id  INTEGER PRIMARY KEY,
    company_id  INTEGER NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    vacancy_name VARCHAR(255) NOT NULL,
    salary_from INTEGER CHECK (salary_from >= 0),
    salary_to   INTEGER CHECK (salary_to >= 0),
    url         VARCHAR(500),
    CONSTRAINT salary_range CHECK (
        salary_to IS NULL OR salary_from IS NULL OR salary_to >= salary_from
    )
);
