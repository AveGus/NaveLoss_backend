from django.db import models
from django.contrib.auth.models import User


class CarInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.CharField(blank=False, max_length=255)
    longitude = models.CharField(blank=False, max_length=255)
    comment = models.TextField(blank=True)


