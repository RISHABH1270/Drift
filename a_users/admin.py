"""
👤 USERS ADMIN CONFIGURATION - Profile Management Interface 👤

This file registers the Profile model with Django's admin interface, allowing administrators to view and manage user profiles through the web-based admin panel.

🎯 ADMIN ACCESS:
1. Visit: http://127.0.0.1:8000/admin/
2. Login as superuser
3. See "Profiles" section to manage user profiles
"""

from django.contrib import admin   # Django's admin system
from .models import Profile        # Our custom Profile model

# 📝 REGISTER PROFILE MODEL FOR ADMIN INTERFACE
# This creates a basic admin interface for Profile model
admin.site.register(Profile)

# 💡 WHAT THIS GIVES YOU:
# - List view of all profiles
# - Add new profile form
# - Edit existing profile form  
# - Delete profiles
# - Search and filter capabilities (basic)