from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path("test/", views.test_view),  # Route to your test_view
]
