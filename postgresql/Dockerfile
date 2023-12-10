FROM postgres:latest

# Настройки базы данных
ENV POSTGRES_DB=atom_bot_project
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=0052533

# Копируем инициализационные SQL-скрипты в директорию, которая будет автоматически выполнена при запуске контейнера
COPY init.sql /docker-entrypoint-initdb.d/
