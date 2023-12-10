# Используем базовый образ с Python
FROM python:3.8

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в образ
COPY . /app/

# Команда для запуска Celery
CMD ["celery", "-A", "settings_app", "worker", "--loglevel=info"]
