from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def start_career_choice(request):
    """
    Renders the main career choice landing page.
    
    The template path 'careerland.html' tells Django to look for a template
    with this name in the 'templates' folder of any installed app.
    """
    return render(request, 'careerland.html')

def custom_logout(request):
    logout(request)
    return redirect("templates/careerland.html")  # redirects to the named careerland url