"""
👤 USER APP VIEWS - Profile & Account Management Controllers 👤

This file contains all the view functions that handle user profile and account 
management functionality. These are more complex views that demonstrate various 
Django concepts like authentication, form handling, HTMX integration, etc.

🎯 VIEW TYPES DEMONSTRATED:
- Simple template rendering
- Form handling (GET and POST)
- Authentication requirements (@login_required)  
- Dynamic routing (username parameter)
- HTMX partial rendering
- User feedback messages
- Account deletion with confirmation
"""

# 🎯 IMPORTS - All the tools we need for complex views
from django.shortcuts import render, redirect, get_object_or_404  # Common view helpers
from django.urls import reverse                    # Generate URLs from URL names
from allauth.account.utils import send_email_confirmation  # Email verification
from django.contrib.auth.decorators import login_required  # Require login
from django.contrib.auth import logout             # Log user out
from django.contrib.auth.models import User        # User model
from django.contrib.auth.views import redirect_to_login  # Redirect to login page
from django.contrib import messages                # User feedback messages
from .forms import *                               # Import all forms from this app

def profile_view(request, username=None):
    """
    👤 PROFILE VIEW - Display user profiles (public or own)
    
    This view handles TWO different scenarios:
    1. Public profile: /profile/john_doe/ (shows john_doe's profile to anyone)
    2. Own profile: /profile/ (shows current user's profile to themselves)
    
    📋 PARAMETERS:
    - request: Standard HTTP request object
    - username: Optional - if provided, show that user's profile
    
    🎯 LOGIC FLOW:
    1. If username provided → Show that user's public profile
    2. If no username → Show current user's own profile  
    3. If user not logged in → Redirect to login page
    """
    
    if username:
        # 🌐 PUBLIC PROFILE SCENARIO
        # Someone is viewing another user's profile via URL like /@john_doe/
        # get_object_or_404 = Find user OR show 404 page if not found
        profile = get_object_or_404(User, username=username).profile
    else:
        # 👤 OWN PROFILE SCENARIO  
        # User is viewing their own profile via /profile/
        try:
            # Try to access the current user's profile
            profile = request.user.profile
        except:
            # If they're not logged in or have no profile, redirect to login
            # request.get_full_path() = Remember where they were trying to go
            return redirect_to_login(request.get_full_path())
    
    # 📄 RENDER THE TEMPLATE
    # Pass the profile data to the template so it can display user info
    return render(request, 'a_users/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    """
    ✏️ PROFILE EDIT VIEW - Handle profile editing form
    
    This demonstrates the STANDARD Django form handling pattern:
    1. GET request → Show empty/pre-filled form
    2. POST request → Process submitted form data
    3. Valid data → Save and redirect
    4. Invalid data → Show form again with errors
    
    🔒 SECURITY: @login_required decorator ensures only logged-in users can access
    
    🎯 DUAL PURPOSE: 
    - Regular editing: /profile/edit/
    - New user onboarding: /profile/onboarding/
    """
    
    # 📝 STEP 1: CREATE FORM INSTANCE
    # Pre-populate form with user's current profile data
    # instance=request.user.profile means "edit this existing profile"
    form = ProfileForm(instance=request.user.profile)
    
    # 📨 STEP 2: CHECK REQUEST METHOD
    if request.method == 'POST':
        # 📥 FORM SUBMISSION - User clicked submit button
        
        # Create form with submitted data AND files (for image uploads)
        # request.POST = text data (name, bio, etc.)
        # request.FILES = uploaded files (profile picture)
        # instance= tells Django which existing object to update
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        # 🔍 STEP 3: VALIDATE SUBMITTED DATA
        if form.is_valid():
            # ✅ DATA IS VALID - Save changes and redirect
            form.save()  # Updates the database
            return redirect('profile')  # Go back to profile page
            
        # ❌ If form.is_valid() is False, we fall through to render the form
        # again with error messages attached
    
    # 🎭 STEP 4: DETERMINE CONTEXT (Onboarding vs Regular Edit)
    # Check if this is first-time setup or regular editing
    if request.path == reverse('profile-onboarding'):
        onboarding = True   # Show "Complete your profile" messaging
    else:
        onboarding = False  # Show "Edit your profile" messaging
    
    # 📄 STEP 5: RENDER TEMPLATE
    # Pass form and onboarding flag to template
    context = {
        'form': form,           # Form object (with data and/or errors)
        'onboarding': onboarding  # Boolean for template conditional logic
    }
    return render(request, 'a_users/profile_edit.html', context)

@login_required
def profile_settings_view(request):
    return render(request, 'a_users/profile_settings.html')

@login_required
def profile_emailchange(request):
    """
    📧 EMAIL CHANGE VIEW - HTMX-powered email updating
    
    This demonstrates ADVANCED Django concepts:
    - HTMX integration (partial page updates without full refresh)
    - Duplicate validation (prevent multiple users with same email)
    - Email verification workflow
    - User feedback messages
    
    🎯 HTMX FLOW:
    1. User clicks "Change Email" → HTMX sends GET request
    2. request.htmx = True → Return just the form HTML (not full page)
    3. HTMX replaces part of page with form
    4. User submits → POST request → Process form → Success message
    """
    
    # ⚡ HTMX REQUEST - Return partial template (just the form)
    if request.htmx:
        # Create form pre-filled with current email
        form = EmailForm(instance=request.user)
        # Return ONLY the form HTML, not full page template
        return render(request, 'partials/email_form.html', {'form': form})
    
    # 📨 FORM SUBMISSION - Process the email change
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():
            # 🔍 DUPLICATE EMAIL VALIDATION
            # Check if another user already has this email address
            email = form.cleaned_data['email']  # Get the cleaned/validated email
            
            # Query: Find users with this email, BUT exclude current user
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                # 🚫 EMAIL ALREADY TAKEN - Show error message
                messages.warning(request, f'{email} is already in use.')
                return redirect('profile-settings')
            
            # ✅ EMAIL IS AVAILABLE - Save the change
            form.save()  # Updates user.email in database
            
            # 🔄 AUTOMATIC SIGNAL PROCESSING
            # Our post_save signal automatically:
            # - Updates EmailAddress model
            # - Sets email as unverified (since it changed)
            
            # 📧 SEND VERIFICATION EMAIL
            # User must verify their new email address
            send_email_confirmation(request, request.user)
            
            # 🎉 SUCCESS - Redirect back to settings with success message
            return redirect('profile-settings')
        else:
            # ❌ FORM VALIDATION FAILED - Show error
            messages.warning(request, 'Email not valid or already in use')
            return redirect('profile-settings')
    
    # 🔄 DEFAULT - Redirect back to settings page
    # This handles any unexpected request types
    return redirect('profile-settings')


@login_required
def profile_usernamechange(request):
    if request.htmx:
        form = UsernameForm(instance=request.user)
        return render(request, 'partials/username_form.html', {'form':form})
    
    if request.method == 'POST':
        form = UsernameForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Username updated successfully.')
            return redirect('profile-settings')
        else:
            messages.warning(request, 'Username not valid or already in use')
            return redirect('profile-settings')
    
    return redirect('profile-settings')    


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect('profile-settings')

@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted')
        return redirect('home')
    
    return render(request, 'a_users/profile_delete.html')