FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта в рабочую директорию контейнера
COPY . /app/

# Команда для выполнения миграций и запуска сервера
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# Устанавливаем переменные окружения
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}
ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
ENV CELERY_BROKER=${CELERY_BROKER}
ENV TELEGRAM_BOT_API_KEY=${TELEGRAM_BOT_API_KEY}
ENV SECRET_KEY=${SECRET_KEY}
