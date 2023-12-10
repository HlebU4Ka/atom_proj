# My Django Project

## Запуск проекта в Docker-контейнере

1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Склонируйте репозиторий: `git clone https://github.com/your_username/your_project.git`
3. Перейдите в директорию проекта: `cd your_project`
4. Создайте и примените миграции: `docker-compose run django python manage.py migrate`
5. Запустите проект: `docker-compose up`
6. Откройте браузер и перейдите по адресу `http://localhost:8000/`
