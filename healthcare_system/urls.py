

from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Healthcare Admin"
admin.site.site_title = "Healthcare Admin Portal"
admin.site.index_title = "Welcome to My Healthcare Admin Dashboard"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
    path('', include('appointments.urls', namespace='appointments')),
   

    

]
