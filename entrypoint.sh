#!/usr/bin/env bash
set -e

# 1️⃣ Apply migrations
python manage.py migrate --noinput

# 2️⃣ Create superuser only if the table is empty
python manage.py shell <<'PY'
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='YourStrongPass!'
    )
    print('Superuser created')
else:
    print('Superuser already exists')
PY

# 3️⃣ Start the app
exec gunicorn kindle_shop.wsgi:application "$@"
