CREATE TABLE IF NOT EXISTS companies (
    id      INTEGER PRIMARY KEY,
    name    VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS vacancies (
    id          INTEGER PRIMARY KEY,
    company_id  INTEGER NOT NULL REFERENCES companies(id) ON DELETE CASCADE,
    name        VARCHAR(255) NOT NULL,
    salary_from INTEGER CHECK (salary_from >= 0),
    salary_to   INTEGER CHECK (salary_to >= 0),
    url         VARCHAR(500),
    CONSTRAINT salary_range CHECK (
        salary_to IS NULL OR salary_from IS NULL OR salary_to >= salary_from
    )
);
