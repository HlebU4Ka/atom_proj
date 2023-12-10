-- Создание базы данных
CREATE DATABASE atom_bot_project;

-- Создание пользователя и предоставление ему прав доступа
CREATE USER postgres WITH PASSWORD '0052533';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';

-- Предоставление прав доступа пользователю к базе данных
GRANT ALL PRIVILEGES ON DATABASE atom_bot_project TO postgres;
