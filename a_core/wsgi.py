"""
🌐 WSGI CONFIGURATION - Traditional Web Server Interface 🌐

WSGI (Web Server Gateway Interface) is the traditional Python web standard.

🎯 WSGI vs ASGI:
- WSGI: Synchronous, handles one request at a time per thread
- ASGI: Asynchronous, can handle multiple requests concurrently
"""

import os  

from django.core.wsgi import get_wsgi_application

# 🎯 SETTINGS MODULE CONFIGURATION
# Tell Django where to find the settings file
# Same as asgi.py but for WSGI servers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

# 🌐 CREATE WSGI APPLICATION
# This creates the application object for traditional web servers
# Apache with mod_wsgi, Gunicorn, uWSGI all use this
application = get_wsgi_application()

# 💡 IN PRODUCTION, THIS IS USED LIKE:
# gunicorn a_core.wsgi:application --bind 0.0.0.0:8000
# Apache WSGIModule a_core.wsgi:application

# 🤔 WHEN TO USE WSGI vs ASGI:
# - Use WSGI for traditional Django apps (most common)
# - Use ASGI if you need WebSockets, async views, or Django Channels
