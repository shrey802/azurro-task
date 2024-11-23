import uuid
from django.db import models

class Owner(models.Model):
    turf_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    turf_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.turf_name})"


class Booking(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    owner_turf_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="bookings")
    turf_name = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.username} on {self.date} for {self.turf_name}"
