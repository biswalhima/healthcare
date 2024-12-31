from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin

from django.conf import settings  # Import settings to reference the custom user model

# from django.contrib.auth.models import User




class User(AbstractUser):
    ROLES = (
        # ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    
    role = models.CharField(max_length=100, choices=ROLES,default='patient')

    # Specify unique related_name attributes for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    # Appointment model to store booking details
class Appointment(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='appointments_as_doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='appointments_as_patient', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.CharField(max_length=500)

    def __str__(self):
        return f'Appointment with {self.doctor.username} for {self.patient.username} on {self.appointment_date}'
