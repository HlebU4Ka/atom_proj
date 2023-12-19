-- Создание базы данных
CREATE DATABASE ${POSTGRES_DB_NAME};

-- Создание пользователя и предоставление ему прав доступа
CREATE USER postgres WITH PASSWORD ${DB_PASSWORD};
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';

-- Предоставление прав доступа пользователю к базе данных
GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB_NAME} TO ${POSTGRES_USER_NAME};
