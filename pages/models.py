from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _


class ContactUsModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    topic = models.CharField(max_length=300, verbose_name=_('topic'))
    text = models.TextField(verbose_name=_('text'))
    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'), )

    class Meta:
        verbose_name = _('contact_us_form')
        verbose_name_plural = _("contact_us_form")
        ordering = ['datetime_created']
