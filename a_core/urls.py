"""
🗺️ MAIN URL CONFIGURATION - The GPS System of Your Django App! 🗺️

This is the MASTER routing file - think of it as the main reception desk that
directs visitors to the right department in a big building.

🎯 HOW IT WORKS:
1. User visits: https://yoursite.com/profile/
2. Django looks at this file
3. Finds: path('profile/', include('a_users.urls'))
4. Directs request to a_users/urls.py for further routing
5. The appropriate view function handles the request
6. HTML response is sent back to user's browser
"""

# 🎯 IMPORTS - Bringing in the routing tools
from django.contrib import admin                    # Django's admin panel
from django.urls import path, include               # URL routing functions
from a_home.views import *                          # Import all views from home app
from django.conf import settings                    # Access to project settings
from django.conf.urls.static import static          # For serving uploaded files
from a_users.views import profile_view              # Specific view for user profiles

# 🗺️ URL PATTERNS - The Main Directory
# =====================================
# Each path() is like a street sign pointing to the right destination

urlpatterns = [
    # 👨‍💼 ADMIN PANEL - Django's built-in management interface
    # URL: /admin/
    # Goes to: Django's admin interface (like WordPress admin)
    path('admin/', admin.site.urls),
    
    # 🔐 AUTHENTICATION - Login, logout, signup, password reset
    # URLs: /accounts/login/, /accounts/logout/, /accounts/signup/, etc.
    # Goes to: Allauth's pre-built authentication views
    path('accounts/', include('allauth.urls')),
    
    # 🏠 HOMEPAGE - The front door of your website
    # URL: / (root URL, like https://yoursite.com/)
    # Goes to: home_view function in a_home/views.py
    path('', home_view, name="home"),
    
    # 👤 USER PROFILES - All profile-related pages
    # URLs: /profile/, /profile/edit/, /profile/settings/, etc.
    # Goes to: a_users/urls.py for further routing
    path('profile/', include('a_users.urls')),
    
    # 🌐 PUBLIC PROFILE PAGES - Like social media profile URLs
    # URL: /@username/ (e.g., /@john_doe/)
    # Goes to: profile_view function with username parameter
    path('@<username>/', profile_view, name="profile"),
]

# 📸 MEDIA FILES SERVING - For Development Only
# =============================================
# This serves uploaded files (profile pictures, etc.) during development
# In production, your web server (Apache/Nginx) handles this

# Only works when DEBUG=True (development mode)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 💡 EXPLANATION:
# - settings.MEDIA_URL = '/media/' (the URL prefix)
# - settings.MEDIA_ROOT = '/path/to/your/project/media/' (the folder on disk)
# So /media/profile_pics/john.jpg → serves file from /path/to/project/media/profile_pics/john.jpg
