# Drift
Django WebSocket chat platform for real-time messaging.

## Status
✅ **Initial Setup Complete** - Django 5.2.4 + Python 3.13.4

## Done
- Django project created (`a_core`)
- Virtual environment configured
- Dependencies installed: Django, django-allauth, django-htmx, Pillow
- Git repository initialized on `development` branch
- README documentation updated

## Structure
```
Drift/
├── a_core/          # Django core project
├── manage.py        # Django commands
├── requirements.txt # Dependencies
├── venv/           # Virtual environment
└── .git/           # Version control
```

## Quick Start
```bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Next Steps
1. Run migrations
2. Commit current files
3. Create chat/users apps
4. Add WebSocket support
5. Build messaging features