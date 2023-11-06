from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # add custom filed
    age = models.PositiveIntegerField()
