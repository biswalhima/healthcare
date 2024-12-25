# appointments/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from appointments.models import User  # Import your custom user model

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User  # Use the custom user model
        fields = ['username', 'email', 'password1', 'password2', 'role']
