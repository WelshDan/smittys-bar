from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=128, default="password")
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email