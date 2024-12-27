from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Appointment

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'appointment_date', 'reason')
    list_filter = ('appointment_date', 'doctor', 'patient')
    search_fields = ('doctor__username', 'patient__username', 'reason')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Appointment, AppointmentAdmin)
