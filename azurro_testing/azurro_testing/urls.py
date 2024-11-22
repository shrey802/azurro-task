
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theapp.urls')),  # Ensure this includes theapp's URLs
]