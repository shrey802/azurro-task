from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings


# Create your models here.

class EnterpriseUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.company_name})"

class Turf(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name of the turf
    location = models.TextField()  # Location of the turf
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='turfs'
    )  # Link to the owner (EnterpriseUser)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the turf was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the turf was last updated

    def __str__(self):
        return self.name