"""
DJANGO TESTING FRAMEWORK - Automated Testing for Home App

Testing is like having a robot check your code automatically.
Django provides tools to write tests that verify your code works correctly.

TEST TYPES:
1. Unit Tests - Test individual functions/methods
2. Integration Tests - Test how different parts work together
3. Functional Tests - Test user workflows from start to finish
"""

from django.test import TestCase             # Django's testing framework
from django.urls import reverse              # For testing URL routing
from django.contrib.auth.models import User  # For testing with users

# CREATE YOUR TESTS HERE

# HOW TO RUN TESTS:
# python manage.py test                    # Run all tests
# python manage.py test a_home             # Run tests for home app
