
-- Users are handled by Django's auth_user table
CREATE TABLE auth_user (
    id INTEGER PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL
);

CREATE TABLE auth_userrole (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES auth_user(id),
    role VARCHAR(10) NOT NULL CHECK (role IN ('teacher', 'student'))
);

CREATE TABLE api_journal (
    id INTEGER PRIMARY KEY,
    teacher_id INTEGER NOT NULL REFERENCES auth_user(id),
    description TEXT NOT NULL,
    attachment_type VARCHAR(10),
    attachment VARCHAR(100),
    published_at DATETIME,
    is_published BOOLEAN DEFAULT FALSE
);

CREATE TABLE api_journal_tagged_students (
    id INTEGER PRIMARY KEY,
    journal_id INTEGER REFERENCES api_journal(id),
    user_id INTEGER REFERENCES auth_user(id)
);
