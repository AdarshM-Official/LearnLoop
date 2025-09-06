from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate

def auth_view(request):
    login_form = LoginForm(request.POST or None)
    signup_form = SignupForm(request.POST or None)

    if request.method == 'POST':
        if request.POST.get('form_type') == 'login' and login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('start_choice')
            else:
                login_form.add_error(None, "Invalid username or password.")

        elif request.POST.get('form_type') == 'signup' and signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                signup_form.add_error('username', 'This username is already taken.')
            else:
                # Create the new user
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect('start_choice')

    return render(request, 'registration/login.html', {
        'login_form': login_form,
        'signup_form': signup_form
    })
