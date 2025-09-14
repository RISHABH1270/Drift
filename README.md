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

## Django Project Structure:
```
Drift/                            # 🏠 Your main project folder
  ├── manage.py                   # 🔧 Django's command-line tool
  ├── requirements.txt            # 📋 List of Python packages needed
  ├── db.sqlite3                  # 💾 Your database file (like a filing cabinet)
  ├── a_core/                     # ⚙️  Main project configuration (the brain)
  ├── a_home/                     # 🏡 Home page app
  ├── a_users/                    # 👤 User management app
  ├── templates/                  # 🎨 HTML templates (the face of your website)
  ├── static/                     # 📁 CSS, JS, images (styling and assets)
  ├── media/                      # 📸 User uploaded files (profile pics, etc.)
  └── venv/                       # 🛡️  Virtual environment (isolated Python world)
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