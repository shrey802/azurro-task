from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.

class EnterpriseUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.company_name})"