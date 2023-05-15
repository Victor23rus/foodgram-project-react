# Foodgram-project-react

![example workflow](https://github.com/Victor23rus/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Описание:
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
Проект доступен по адресу: http://130.193.52.43/
## Технологии:

Python, Django, Django Rest Framework, Docker, Gunicorn, NGINX, PostgreSQL, Yandex Cloud

## Запуск проекта в контейнерах:

Клонировать репозиторий:
```bash
git clone @github.com:Victor23rus/foodgram-project-react.git
cd infra
```
В директории /infra создайте файл .env, с переменными окружения:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Сборка и развертывание контейнеров:
```bash
docker-compose up -d --build
```
Выполните миграции, соберите статику, создайте суперпользователя:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --no-input
docker-compose exec backend python manage.py createsuperuser
```
Наполните базу данных ингредиентами и тегами:
```bash
docker-compose exec -it backend python manage.py loaddata dump.json 
```
# Примеры работы эндпоинтов:
Список рецептов
{
    "users": "http://130.193.52.43/api/users/",
    "ingredients": "http://130.193.52.43/api/ingredients/",
    "tags": "http://130.193.52.43/api/tags/",
    "recipes": "http://130.193.52.43/api/recipes/"
}

  [POST].../api/users/auth/
  {
    "username": "SneakyFox",
    "password": "1234567bb"
}

Примерный ответ:

{"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MjA5NTYwNywianRpIjoiMDBmMGI0MG.sE5Bd3vrnQLIAL5GxxFg36tPoYyB9I5MQBE_iGshpK4",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk1NjA3LCJqdGkiOiI0YmIxN2MzODcwNGU0YzQ0OWQ4Nzg4NzA4ODcyZTliMCIsInVzZXJfaWQiOjF9"
}
## Документация:
http://130.193.52.43/api/docs

## Логин пароль в админ зону

victor918@mail.ru - Login
123 -Password

## Автор

Виктор Шилигин