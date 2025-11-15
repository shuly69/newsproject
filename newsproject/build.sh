#!/bin/bash

set -e

# Функция ожидания базы данных


# Применяем миграции
echo "Applying migrations..."
python manage.py migrate --noinput

# Создаем суперпользователя
echo "Creating superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
    print('Superuser created')
else:
    print('Superuser already exists')
"

# Запускаем сервер
echo "Starting server..."
exec "$@"