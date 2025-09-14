"""
DJANGO FORMS - User Input Validation and HTML Generation

Forms in Django are like smart HTML form builders. They:
1. Generate HTML form fields automatically
2. Validate user input (check if email is valid, etc.)
3. Convert form data to Python objects
4. Handle file uploads
5. Provide security (CSRF protection)

FORM TYPES:
- Form: Build forms from scratch with individual fields
- ModelForm: Automatically create forms from Django models (most common)
"""

# IMPORTS - Tools needed for forms
from django.forms import ModelForm   # Base class for model-based forms
from django import forms            # Individual form field types
from django.contrib.auth.models import User  # Django's user model
from .models import Profile         # Our custom profile model


class ProfileForm(ModelForm):
    """
    PROFILE EDITING FORM - Let users update their profile info
    
    This form automatically generates HTML form fields based on the
    Profile model fields. It handles image uploads, text input, and
    textarea for the bio.
    
    USAGE IN VIEWS:
    form = ProfileForm(instance=user.profile)  # Pre-fill with existing data
    form = ProfileForm(request.POST, request.FILES, instance=user.profile)  # Process submission
    """
    
    class Meta:
        # FORM CONFIGURATION CLASS
        # Meta class tells Django how to build the form
        
        # Which model to base the form on
        model = Profile
        
        # Which fields from the model to include in the form
        fields = ['image', 'displayname', 'info']
        
        # CUSTOM HTML WIDGETS - Control how fields are rendered
        widgets = {
            # File upload widget for profile pictures
            'image': forms.FileInput(),
            
            # Text input with placeholder text
            'displayname': forms.TextInput(attrs={
                'placeholder': 'Add display name'
            }),
            
            # Textarea with custom rows and placeholder
            'info': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Add information'
            })
        }
        
        
class EmailForm(ModelForm):
    """
    EMAIL CHANGE FORM - Let users update their email address
    
    This form is based on Django's User model but only shows the email field.
    It includes extra validation to ensure the email is properly formatted.
    
    EXTRA VALIDATION:
    - required=True ensures email can't be empty
    - EmailField automatically validates email format (user@domain.com)
    """
    
    # CUSTOM FIELD DEFINITION
    # Override the default email field with extra validation
    email = forms.EmailField(required=True)

    class Meta:
        # Base form on Django's User model
        model = User
        
        # Only include email field
        fields = ['email']


class UsernameForm(ModelForm):
    """
    USERNAME CHANGE FORM - Let users update their username
    
    Simple form for changing usernames. Based on Django's User model.
    The username field has built-in validation (unique, proper characters).
    """
    
    class Meta:
        # Base form on Django's User model
        model = User
        
        # Only include username field
        fields = ['username']

# HOW DJANGO FORMS WORK:
# 
# 1. FORM CREATION:
#    form = ProfileForm()  # Empty form for GET requests
#    form = ProfileForm(instance=profile)  # Pre-filled form
# 
# 2. FORM SUBMISSION:
#    form = ProfileForm(request.POST, request.FILES)
#    
# 3. VALIDATION:
#    if form.is_valid():  # Runs all validation rules
#        form.save()      # Saves to database
#    else:
#        # Form has errors, show them to user
#
# 4. IN TEMPLATES:
#    {{ form.as_p }}      # Render all fields with <p> tags
#    {{ form.displayname }}  # Render specific field
#    {{ form.displayname.errors }}  # Show field errors
#
# 5. FORM SECURITY:
#    - CSRF tokens automatically added
#    - Input sanitization
#    - SQL injection prevention
#    - File upload security