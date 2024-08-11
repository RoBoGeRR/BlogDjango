from django.contrib.auth import get_user_model
import os

User = get_user_model()

# Superuser credentials
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'serg')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '1701Dn')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'serg@gmail.com')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print(f'Superuser "{username}" created.')
else:
    print(f'Superuser "{username}" already exists.')
