# your_app/forms.py

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username or Email',
                'id': 'id_login_username' # Unique ID for login form
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'id_login_password' # Unique ID for login form
            }
        )
    )

class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Choose a Username',
                'id': 'id_signup_username' # Unique ID for signup form
            }
        )
    )
    email = forms.EmailField( # Added email field
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address',
                'id': 'id_signup_email' # Unique ID for signup form
            }
        )
    )
    profile_img = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'placeholder': 'Upload Profile Image',
            'id': 'id_signup_profileimg'
        })
    ) # Added profile image field


    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Create Password',
                'id': 'id_signup_password' # Unique ID for signup form
            }
        )
    )
    password_confirm = forms.CharField( # Added password confirm
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
                'id': 'id_signup_password_confirm' # Unique ID for signup form
            }
        )
    )

    # Optional: Add a clean method for password confirmation in Django form
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data