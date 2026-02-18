# Простой корпоративный Django-портал

Минимальный Django-проект с авторизацией и сессиями.

## Что внутри

- страница входа и регистрации,
- личный кабинет (редактирование имени, фамилии, email и блока «о себе»),
- раздел «Мои задачи» (добавить / отметить выполненной / удалить),
- раздел «Доска команды» (публикация коротких объявлений),
- стартовая страница портала с новостями.

> Дополнения пользователя (bio, задачи, объявления) хранятся в сессии для простоты примера.

## Запуск (Linux/macOS)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Запуск (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте http://127.0.0.1:8000/
