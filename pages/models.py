from django.db import models

from django.utils.translation import gettext_lazy as _


class ContactUsModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    topic = models.CharField(max_length=300, verbose_name=_('topic'))
    text = models.TextField(verbose_name=_('text'))
