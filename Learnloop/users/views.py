# your_app/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages  # <<< 1. IMPORT MESSAGES
from .forms import LoginForm, SignupForm # Make sure your forms are imported correctly

def auth_view(request):
    if request.method == 'POST':
        # Initialize forms with POST data
        login_form = LoginForm(request.POST)
        signup_form = SignupForm(request.POST)

        if request.POST.get('form_type') == 'login':
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    # <<< 2. ADD SUCCESS MESSAGE FOR LOGIN
                    messages.success(request, f'Login Successful! Welcome back, {user.username}.')
                    return redirect('start_choice')
                else:
                    # <<< 3. ADD ERROR MESSAGE FOR FAILED LOGIN
                    messages.error(request, 'Invalid username or password.')
            # If form is not valid, it will re-render with errors below

        elif request.POST.get('form_type') == 'signup':
            if signup_form.is_valid():
                username = signup_form.cleaned_data['username']
                email = signup_form.cleaned_data['email']
                password = signup_form.cleaned_data['password']

                if User.objects.filter(username=username).exists():
                    # This check is good, but see the "Best Practice" tip below!
                    messages.error(request, 'This username is already taken.')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    login(request, user)
                    # <<< 4. ADD SUCCESS MESSAGE FOR SIGNUP
                    messages.success(request, f'Account created successfully! Welcome to CareerFlow, {user.username}.')
                    return redirect('start_choice')
            # If form is not valid, it will re-render with errors below

    else: # This is a GET request
        login_form = LoginForm()
        signup_form = SignupForm()

    return render(request, 'registration/login.html', {
        'login_form': login_form,
        'signup_form': signup_form
    })