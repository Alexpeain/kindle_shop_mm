#!/usr/bin/env bash
set -e

# 1️⃣ Apply migrations
python manage.py migrate --noinput

# 2️⃣ Create superuser only if the table is empty
python manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser(
        username=os.getenv('DJANGO_SU_USERNAME', 'admin'),
        email=os.getenv('DJANGO_SU_EMAIL', 'admin@example.com'),
        password=os.getenv('DJANGO_SU_PASSWORD', 'YourStrongPass!')
    )
    print('Superuser created')
else:
    print('Superuser already exists')
PY

# 3️⃣ Start the app
exec gunicorn kindle_shop.wsgi:application "$@"
