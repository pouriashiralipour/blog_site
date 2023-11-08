from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    # add custom fields
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('age'))
    avatar = models.ImageField(upload_to='user_avatar/', verbose_name=_('avatar'), blank=True, null=True)
