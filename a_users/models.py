"""
📊 USER PROFILE MODEL - Database Blueprint for User Profiles 📊

Models in Django are like blueprints for database tables. They define:
- What information to store (fields)
- How that information relates to other data (relationships)
- Rules for the data (validation, constraints)

Think of a model as designing a form - you decide what fields it should have,
what type of information goes in each field, and what the rules are.
"""

from django.db import models                   # Django's model system
from django.contrib.auth.models import User    # Django's built-in User model
from django.templatetags.static import static  # For accessing static files
from django.conf import settings               # Project settings


class Profile(models.Model):
    """
    👤 USER PROFILE MODEL - Extended User Information
    
    Django's built-in User model only has basic info (username, email, password).
    This Profile model extends it with additional information like profile picture,display name, and info.
    
    🎯 DATABASE RELATIONSHIP:
    - Each User has exactly ONE Profile (OneToOne)
    - Each Profile belongs to exactly ONE User
    - If User is deleted, their Profile is also deleted (CASCADE)
    
    """
    
    # 🔗 RELATIONSHIP FIELD - Links this profile to a Django User
    # OneToOneField = Each user has exactly one profile, each profile has exactly one user
    # on_delete=CASCADE = If the user is deleted, delete this profile too
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # 🖼️ PROFILE PICTURE FIELD
    # ImageField = Handles image uploads with validation
    # upload_to='avatars/' = Save uploaded images in media/avatars/ folder  
    # null=True = Database can store NULL (empty) values
    # blank=True = Django forms can submit this field empty
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    # 📝 DISPLAY NAME FIELD
    # CharField = Text field with a maximum length
    # max_length=20 = Can't be longer than 20 characters
    # null=True, blank=True = Optional field
    displayname = models.CharField(max_length=20, null=True, blank=True)
    
    # 📄 INFO FIELD  
    # TextField = Large text field (for paragraphs)
    # null=True, blank=True = Optional field
    info = models.TextField(null=True, blank=True)
    
    def __str__(self):
        """
        🏷️ STRING REPRESENTATION
        This method determines how the Profile object appears when printed or 
        displayed in Django admin. Returns the username of the associated user.
        
        Example: If user's username is 'john_doe', this returns 'john_doe'
        """
        return str(self.user)
    
    @property
    def name(self):
        """
        🎭 NAME PROPERTY - Smart Display Name
        
        A @property decorator makes this method work like a variable.
        You can use profile.name instead of profile.name()
        
        🎯 LOGIC:
        - If user set a custom display name → use that
        - If no display name → use their username as fallback
        
        Example:
        - displayname = "John Smith" → returns "John Smith"  
        - displayname = None → returns "john_doe" (username)
        """
        if self.displayname:
            return self.displayname
        return self.user.username
    
    @property 
    def avatar(self):
        """
        🖼️ AVATAR PROPERTY - Smart Profile Picture
        
        Returns the URL to the user's profile picture, with a fallback
        to a default avatar if they haven't uploaded one.
        
        🎯 LOGIC:
        - If user uploaded a picture → return URL to their image
        - If no picture → return URL to default avatar SVG
        
        Example:
        - Has image → returns "/media/avatars/user123.jpg"
        - No image → returns "/static/images/avatar.svg"
        """
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg'

# 💡 UNDERSTANDING THE RELATIONSHIP:
# 
# USER MODEL (Django built-in)     |  PROFILE MODEL (Our custom model)
# -------------------------------- | ----------------------------------
# - username                       | - image (profile picture)  
# - email                          | - displayname (custom name)
# - password                       | - info (bio/description)
# - first_name                     | - user (link back to User)
# - last_name                      |
# - is_active                      |
# - date_joined                    |
#
# 🔗 They are connected by: Profile.user → User
# 
# In code:
# user = User.objects.get(username='john')
# profile = user.profile  # Access the profile
# profile.name  # Get the smart display name
# profile.avatar  # Get profile picture URL