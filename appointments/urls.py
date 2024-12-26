
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'appointments'  # Declare the namespace

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
    path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),  # Add this line for book_appointment URL
    path('logout/', LogoutView.as_view(), name='logout'),

    path('appointments/', views.appointments, name='appointments'),  # This is where the appointments will be displayed


]
