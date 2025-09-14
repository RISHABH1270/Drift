#!/usr/bin/env python
"""
🔧 MANAGE.PY - Django's Magic Wand! 🔧

This is Django's command-line utility - think of it as your project's remote control!
You use it to Run administrative tasks:
- Start the server: python manage.py runserver
- Create database tables: python manage.py migrate  
- Create new apps: python manage.py startapp myapp
- Create admin users: python manage.py createsuperuser
- And much more!
"""

# Import required Python modules
import os    # For operating system interactions (file paths, environment variables)
import sys   # For system-specific parameters and functions


def main():
    """
    🎯 MAIN FUNCTION - The Starting Point
    This function runs when you type 'python manage.py [command]'
    """
    
    # 🎯 Tell Django where to find our project settings
    # This points to 'a_core/settings.py' file
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')
    
    try:
        # 🚀 Import Django's command execution engine
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 🚨 If Django isn't installed, show a helpful error message
        raise ImportError(
            "❌ Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # 🎬 Execute the command you typed (like 'runserver', 'migrate', etc.)
    # sys.argv contains the command-line arguments you typed
    execute_from_command_line(sys.argv)


# 🎭 Python's special way of saying "only run this if this file is executed directly"
# (not imported by another file)
if __name__ == '__main__':
    main()
