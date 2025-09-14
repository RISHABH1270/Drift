"""
🎬 HOME APP VIEWS - The Homepage Functions🏠

They coordinate everything to create the final scene (web page) that users see. When someone visits a URL, Django calls the corresponding view function.

🎯 VIEW FUNCTION FLOW:
1. User visits a URL (e.g., https://yoursite.com/)
2. Django's URL system finds the matching view function
3. View function processes the request
4. View function returns an HTTP response (usually HTML)
5. Browser displays the response to the user
"""

from django.shortcuts import render

# 🏠 HOMEPAGE VIEW - The Front Door
def home_view(request):
    context = {
        'welcome_message': 'Welcome to Drift!',
    }
    return render(request, 'home.html', context)

"""
    This is the simplest possible Django view. It handles requests to the 
    homepage (/) and returns the rendered home.html template.
    
    🎯 WHAT HAPPENS:
    1. Django calls this function when someone visits "/"
    2. render() function finds the 'home.html' template
    3. Template is processed and converted to HTML
    4. HTML is sent back to the user's browser
    
    💡 THE render() FUNCTION:
    - render(request, template_name, context_dict)
    - request: Pass along the request object
    - template_name: Which HTML template to use
    - context_dict: Data to pass to the template (optional)
"""