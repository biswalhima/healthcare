from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Appointment

User = get_user_model()  # This will retrieve the custom User model

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user
class YourForm(forms.Form):
    # Define form fields here
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment  # The model you will use for storing appointments
        fields = ['doctor', 'patient', 'appointment_date', 'reason']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the doctor field to show only users with 'doctor' role
        self.fields['doctor'].queryset = User.objects.filter(role='doctor')

        # Hide the patient field (this will be set automatically in the view)
        self.fields['patient'].required = False
        self.fields['patient'].widget = forms.HiddenInput()

        # Set the input type for appointment_date to 'datetime-local'
        self.fields['appointment_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})