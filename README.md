# Простой одностраничный Django-сайт

Минимальный Django-проект с одной страницей (`/`), где есть:

- вход в аккаунт,
- регистрация нового аккаунта,
- выход из аккаунта,
- сессии через стандартную систему `django.contrib.sessions`.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте http://127.0.0.1:8000/
