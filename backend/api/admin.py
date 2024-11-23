from django.contrib import admin
from .models import Owner, Booking

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "turf_name", "turf_id")
    search_fields = ("first_name", "last_name", "turf_name")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone", "turf_name", "date", "amount", "owner_turf_id")
    search_fields = ("username", "email", "turf_name")
    list_filter = ("date", "owner_turf_id")
