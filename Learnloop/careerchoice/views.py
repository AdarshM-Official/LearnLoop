from django.shortcuts import render

# Create your views here.
def start_career_choice(request):
    """
    Renders the main career choice landing page.
    
    The template path 'careerland.html' tells Django to look for a template
    with this name in the 'templates' folder of any installed app.
    """
    return render(request, 'careerland.html')

