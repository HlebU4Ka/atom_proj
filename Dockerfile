FROM python:3.8

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в образ
COPY . /app/

# Команда для запуска Django-приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
