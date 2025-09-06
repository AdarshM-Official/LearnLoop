# your_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views # You don't need this for the custom view
from . import views # Make sure you import views like this

urlpatterns = [
    # All commented-out lines can be removed for clarity
    path('auth/', views.auth_view, name='auth_forms'),
    
    # You might want a logout URL later
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]