
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import RegistrationForm
from django import forms
from .forms import YourForm
from pathlib import Path
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')


def role_required(role):
    def decorator(view_func):
        return user_passes_test(lambda user: user.role == role, login_url='/login/')(view_func)
    return decorator

@login_required
@role_required('patient')
def patient_dashboard(request):
    return render(request, 'appointments/patient_dashboard.html')

@login_required
@role_required('doctor')
def doctor_dashboard(request):
    return render(request, 'appointments/doctor_dashboard.html')

@login_required
@role_required('admin')
def admin_dashboard(request):
    return render(request, 'appointments/admin_dashboard.html')
class YourForm(forms.Form):
    # Define form fields here, e.g., 
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
               user = form.save()
               login(request, user)
               return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Replace with your desired page after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
def login_view(request):
    return render(request, 'login.html')