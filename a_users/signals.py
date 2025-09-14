"""
📡 DJANGO SIGNALS - Automatic Actions Based on Events 📡

Signals are Django's way of allowing certain "senders" to notify a set of "receivers" 
when some actions have taken place. Think of them as event listeners or hooks.

🎯 REAL-WORLD ANALOGY:
Imagine a doorbell system:
- When someone presses the doorbell (EVENT) 
- The bell rings inside the house (SIGNAL)
- You automatically get up to answer the door (RECEIVER FUNCTION)

In Django:
- When a User is created (EVENT)
- Django sends a post_save signal (SIGNAL) 
- Our function automatically creates a Profile (RECEIVER FUNCTION)

This ensures that EVERY user automatically gets a profile, without us having to 
remember to create one manually every time!
"""

from django.dispatch import receiver                      # Decorator to mark signal receivers
from django.db.models.signals import post_save, pre_save  # Database operation signals
from allauth.account.models import EmailAddress           # Allauth's email tracking
from django.contrib.auth.models import User               # Django's user model  
from .models import Profile                               # Our custom profile model


@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    """
    🎯 POST-SAVE SIGNAL RECEIVER - Runs AFTER a User is saved
    
    This function automatically runs every time a User object is saved to the database.
    It handles two scenarios: new user creation and existing user updates.
    
    📋 PARAMETERS:
    - sender: The model class that sent the signal (User)
    - instance: The actual User object that was saved
    - created: True if this is a new user, False if updating existing user
    - **kwargs: Any additional keyword arguments
    """
    user = instance  # The User object that was just saved
    
    # 🆕 NEW USER SCENARIO - Automatically create their Profile
    if created:
        """
        When someone signs up, Django creates a User object.
        This signal automatically creates a matching Profile object.
        
        🎯 WHY THIS IS IMPORTANT:
        - Every user needs a profile for extra info (avatar, bio, etc.)
        - Without this, we'd have to remember to create profiles manually
        - This ensures no user is ever without a profile
        """
        Profile.objects.create(
            user=user,  # Link the new profile to this user
            # All other fields (image, displayname, info) are optional
            # so they'll be empty initially - user can fill them later
        )
    else:
        # 🔄 EXISTING USER SCENARIO - Keep email addresses synchronized
        """
        When an existing user updates their email address, we need to:
        1. Update their Allauth EmailAddress record 
        2. Mark their email as unverified (since it changed)
        3. Create an EmailAddress record if one doesn't exist
        """
        try:
            # Try to find their primary email address in Allauth system
            email_address = EmailAddress.objects.get_primary(user)
            
            # If their User.email doesn't match their EmailAddress.email
            if email_address.email != user.email:
                # Update the Allauth email record
                email_address.email = user.email
                email_address.verified = False  # Reset verification status
                email_address.save()
                
        except:
            # If no EmailAddress exists, create one
            # This can happen if user was created before Allauth was installed
            EmailAddress.objects.create(
                user=user,
                email=user.email,
                primary=True,      # This is their main email
                verified=False     # Start as unverified
            )


@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    """
    🎯 PRE-SAVE SIGNAL RECEIVER - Runs BEFORE a User is saved
    
    This function automatically runs every time a User object is about to be 
    saved to the database. It's perfect for data cleanup and validation.
    
    📋 PARAMETERS:
    - sender: The model class that will send the signal (User)
    - instance: The User object that's about to be saved
    - **kwargs: Any additional keyword arguments
    """
    
    # 🔤 NORMALIZE USERNAME - Convert to lowercase
    if instance.username:
        """
        🎯 WHY LOWERCASE USERNAMES:
        - Prevents confusion between 'JohnDoe' and 'johndoe'
        - Makes usernames consistent across the site
        - Follows common web conventions
        - Prevents duplicate accounts with different cases
        
        Example: 
        - User tries to signup with 'JohnSmith123'
        - This automatically converts it to 'johnsmith123'
        - Stored in database as 'johnsmith123'
        """
        instance.username = instance.username.lower()

# 💡 SIGNAL FLOW SUMMARY:
# 
# 1. User signs up → User.objects.create() called
# 2. PRE_SAVE signal fires → user_presave() runs → username lowercased
# 3. User saved to database
# 4. POST_SAVE signal fires → user_postsave() runs → Profile created
# 5. User now has both a User record and a Profile record
#
# 🔄 For existing users:
# 1. User updates their info → user.save() called  
# 2. PRE_SAVE signal fires → username lowercased (if changed)
# 3. User saved to database
# 4. POST_SAVE signal fires → email addresses synchronized
#
# 🎯 THE MAGIC:
# All of this happens automatically - no need to remember to do it manually!