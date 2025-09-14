"""
👤 USER APP URLs - Profile & User Management Routes 👤

This file handles all URLs that start with /profile/
It's included from the main urls.py file when someone visits /profile/*

🔗 URL INHERITANCE:
Main urls.py: path('profile/', include('a_users.urls'))
↳ This file: All patterns below are automatically prefixed with /profile/

So 'edit/' here becomes /profile/edit/ on your website!
"""

from django.urls import path        # URL routing function
from a_users.views import *         # Import all view functions from this app

# 🗂️ USER-RELATED URL PATTERNS
# ============================
# All URLs here are automatically prefixed with /profile/ from main urls.py

urlpatterns = [
    # 👤 USER'S OWN PROFILE PAGE
    # Full URL: /profile/
    # Shows: Current user's profile page with their info, posts, etc.
    path('', profile_view, name="profile"),
    
    # ✏️ EDIT PROFILE PAGE
    # Full URL: /profile/edit/
    # Shows: Form to edit profile info (name, bio, avatar, etc.)
    path('edit/', profile_edit_view, name="profile-edit"),
    
    # 🎯 NEW USER ONBOARDING
    # Full URL: /profile/onboarding/
    # Shows: Same as edit page, but for first-time setup after signup
    # Note: Uses same view function as edit, but different template context
    path('onboarding/', profile_edit_view, name="profile-onboarding"),
    
    # ⚙️ ACCOUNT SETTINGS PAGE
    # Full URL: /profile/settings/
    # Shows: Account settings (change email, username, delete account, etc.)
    path('settings/', profile_settings_view, name="profile-settings"),
    
    # 📧 EMAIL CHANGE HANDLER
    # Full URL: /profile/emailchange/
    # Handles: HTMX requests to change user's email address
    path('emailchange/', profile_emailchange, name="profile-emailchange"),
    
    # 📝 USERNAME CHANGE HANDLER
    # Full URL: /profile/usernamechange/
    # Handles: HTMX requests to change user's username
    path('usernamechange/', profile_usernamechange, name="profile-usernamechange"),
    
    # ✅ EMAIL VERIFICATION SENDER
    # Full URL: /profile/emailverify/
    # Action: Sends email verification to user's current email
    path('emailverify/', profile_emailverify, name="profile-emailverify"),
    
    # 🗑️ DELETE ACCOUNT PAGE
    # Full URL: /profile/delete/
    # Shows: Account deletion confirmation page (danger zone!)
    path('delete/', profile_delete_view, name="profile-delete"),
]

# 💡 UNDERSTANDING URL NAMES:
# The 'name' parameter allows you to reference URLs in templates and views:
# 
# In templates: {% url 'profile-edit' %} → generates /profile/edit/
# In views: reverse('profile-edit') → generates /profile/edit/
# 
# This way, if you change the URL pattern, you only need to update it here,
# not in every template and view that references it!