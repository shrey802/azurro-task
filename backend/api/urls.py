from django.urls import path
from .views import OwnerCreateView, BookingCreateView, BookingByTurfDateView

urlpatterns = [
    path("owners/", OwnerCreateView.as_view(), name="create_owner"),
    path("bookings/", BookingCreateView.as_view(), name="create_booking"),
    path('bookings/by_turf_date/', BookingByTurfDateView.as_view(), name='bookings_by_turf_date'),
]
