
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
    path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),
]
