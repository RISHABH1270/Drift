"""
🚀 ASGI CONFIGURATION - Async Web Server Interface 🚀

ASGI (Asynchronous Server Gateway Interface) is Django's modern way to handle
web requests. It's the newer, more powerful version of WSGI that supports:
- Traditional HTTP requests
- WebSockets (real-time communication)
- Background tasks
- Long-running connections

🎯 WHAT THIS FILE DOES:
This file creates the "application" object that your web server uses to 
communicate with your Django project.
"""

import os

from django.core.asgi import get_asgi_application

# 🎯 SETTINGS MODULE CONFIGURATION
# Tell Django where to find the settings file
# This ensures the same settings are used everywhere
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

# 🌐 CREATE ASGI APPLICATION
# This creates the main application object that handles all requests
# Web servers like Daphne, Uvicorn or Hypercorn will use this
application = get_asgi_application()

# 💡 IN PRODUCTION, THIS IS USED LIKE:
# daphne -b 0.0.0.0 -p 8000 a_core.asgi:application
# uvicorn a_core.asgi:application --host 0.0.0.0 --port 8000
# gunicorn a_core.asgi:application -k uvicorn.workers.UvicornWorker
