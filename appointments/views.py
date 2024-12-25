
from django.contrib.auth.decorators import login_required, user_passes_test


# appointments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm  # This import must match the form file location

def home(request):
    return render(request, 'appointments/home.html')


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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Login the user after successful registration
            login(request, user)
            return redirect('home')  # Redirect to login page or home page
    else:
        form = RegistrationForm()
    return render(request, 'appointments/register.html', {'form': form})