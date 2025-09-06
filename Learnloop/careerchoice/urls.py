# careerchoice/urls.py

from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # When a user comes to the base URL of this app, show the start_career_choice view
    # The name 'start_choice' is the key we will use in the template.
    path('', views.start_career_choice, name='start_choice'),
    path("logout/",LogoutView.as_view(next_page="login"), name="logout",),    
]