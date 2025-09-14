"""
👥 USERS APP CONFIGURATION - User Management App Setup 👥

This file configures the 'a_users' Django app and sets up signal handlers.

🎯 KEY FEATURE: Signal Registration in ready() method
"""

from django.apps import AppConfig  # Base class for app configuration


class AUsersConfig(AppConfig):
    """
    👥 USERS APP CONFIGURATION CLASS
    
    This class configures the users app and importantly, registers the
    signal handlers that automatically create profiles for new users.
    """
    
    # 🔢 DEFAULT AUTO FIELD TYPE
    # When Django creates ID fields automatically, use big integers
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 📛 APP NAME - Must match the app directory name
    name = 'a_users'

    def ready(self):
        """
        🚀 APP INITIALIZATION - Runs when Django starts up
        
        This method is called once Django has loaded all apps and models.
        It's the perfect place to register signal handlers, perform
        initialization tasks, or set up app-specific functionality.
        
        🎯 WHAT HAPPENS HERE:
        1. Django finishes loading all apps and models
        2. Django calls this ready() method
        3. We import a_users.signals module
        4. The @receiver decorators in signals.py register signal handlers
        5. Now whenever a User is created/saved, our signals automatically run
        
        💡 WHY IMPORT HERE AND NOT AT TOP OF FILE:
        - Importing at the top can cause circular import issues
        - Django models might not be ready yet during import
        - ready() method ensures everything is loaded before importing signals
        """
        import a_users.signals  # Register signal handlers for automatic profile creation

# 💡 UNDERSTANDING THE SIGNAL FLOW:
# 
# 1. Django starts up
# 2. Loads all apps and models
# 3. Calls AUsersConfig.ready()
# 4. Imports a_users.signals
# 5. Signal handlers are registered
# 6. Later, when someone signs up:
#    - User.objects.create() is called
#    - Django sends post_save signal
#    - Our signal handler automatically creates Profile
#    - User now has both User record and Profile record
#
# This is why signals are "magical" - they work automatically in the background!
