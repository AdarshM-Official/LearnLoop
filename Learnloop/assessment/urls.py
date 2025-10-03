from django.urls import path
from . import views

urlpatterns = [
    # Displays the code submission interface
    path('skill-assessment/<int:challenge_id>/', views.assessment_view, name='skill_assessment'),
    
    # API endpoint to handle the AJAX form submission and start the task
    path('submit-code/', views.submit_code, name='submit_code'),
    
    # API endpoint to check the status of a long-running task
    path('status/<int:submission_id>/', views.get_submission_status, name='get_submission_status'),
]
