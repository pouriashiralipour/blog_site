from django.contrib import admin

from .models import ContactUsModel


@admin.register(ContactUsModel)
class ArticleAdmin(admin.ModelAdmin):
    pass
