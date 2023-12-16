FROM python:3.8

WORKDIR /app

COPY celery/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}
ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
ENV CELERY_BROKER=${CELERY_BROKER}
ENV TELEGRAM_BOT_API_KEY=${TELEGRAM_BOT_API_KEY}
ENV SECRET_KEY=${SECRET_KEY}
