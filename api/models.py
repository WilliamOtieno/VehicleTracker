from django.db import models
from django.utils import timezone

# Create your models here.


class Location(models.Model):
    coordinates = models.CharField(max_length=100)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id
