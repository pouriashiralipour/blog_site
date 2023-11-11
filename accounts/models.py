from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    # add custom fields
    full_name = models.CharField(max_length=200, verbose_name=_('full_name'), blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('age'))
    avatar = models.ImageField(upload_to='user_avatar/', verbose_name=_('avatar'), blank=True, null=True)
    bio = models.TextField(verbose_name=_('bio'), blank=True, null=True)
    description = models.TextField(verbose_name=_('description'), blank= True, null=True)
