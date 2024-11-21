from django.db import models

# Create your models here.
from django.db import models

class Turf(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name