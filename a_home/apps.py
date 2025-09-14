"""
🏠 HOME APP CONFIGURATION - App Settings & Initialization 🏠

This file configures the 'a_home' Django app. Every Django app needs an AppConfig class that tells Django how to handle the app during startup.

🎯 APPCONFIG PURPOSE:
- Configures app-specific settings
"""

from django.apps import AppConfig 


class AHomeConfig(AppConfig):
    """
    🏠 HOME APP CONFIGURATION CLASS
    
    This class inherits from AppConfig and customizes how Django
    handles the 'a_home' app during project startup.
    """
    
    # 🔢 DEFAULT AUTO FIELD TYPE
    # When Django creates ID fields automatically, use big integers
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 📛 APP NAME - Must match the app directory name
    # This tells Django which app this configuration is for
    name = 'a_home'
