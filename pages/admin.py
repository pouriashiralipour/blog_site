from django.contrib import admin

from .models import ContactUsModel


@admin.register(ContactUsModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'text']
    search_fields = ('topic',)
    ordering = ['-datetime_created']
