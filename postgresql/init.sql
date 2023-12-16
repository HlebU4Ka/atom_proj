-- Создание базы данных
CREATE DATABASE ${DB_NAME};

-- Создание пользователя и предоставление ему прав доступа
CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';
ALTER ROLE ${DB_USER} SET client_encoding TO 'utf8';
ALTER ROLE ${DB_USER} SET default_transaction_isolation TO 'read committed';
ALTER ROLE ${DB_USER} SET timezone TO 'UTC';

-- Предоставление прав доступа пользователю к базе данных
GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};

# Копируем инициализационные SQL-скрипты в директорию, которая будет автоматически выполнена при запуске контейнера
COPY postgresql/init.sql /docker-entrypoint-initdb.d/