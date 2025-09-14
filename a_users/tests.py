"""
USER APP TESTING - Automated Tests for User Features

This file contains tests for user-related functionality like:
- Profile creation and updates
- User registration and authentication
- Form validation
- User permissions

Testing ensures that user features work correctly and don't break
when you make changes to the code.
"""

from django.test import TestCase             # Django's testing framework
from django.urls import reverse              # For testing URL routing
from django.contrib.auth.models import User  # Django's user model
from .models import Profile                  # Our custom profile model
from .forms import ProfileForm, EmailForm, UsernameForm  # Our forms

# CREATE YOUR TESTS HERE

# HOW TO RUN THESE TESTS:
# python manage.py test a_users                    # Run all user app tests
