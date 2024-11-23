from django.urls import path
from .views import OwnerCreateView, BookingCreateView

urlpatterns = [
    path("owners/", OwnerCreateView.as_view(), name="create_owner"),
    path("bookings/", BookingCreateView.as_view(), name="create_booking"),
]
