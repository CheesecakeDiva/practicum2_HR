#!/bin/sh

# миграции в базу PostgreSQL
python manage.py migrate --no-input

# статические файлы для Nginx
python manage.py collectstatic --no-input

# Gunicorn
gunicorn hr_platform.wsgi:application -b 0.0.0.0:8000 --workers 3 --threads 3
