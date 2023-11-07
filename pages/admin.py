from django.contrib import admin

from .models import ContactUsModel, NewsEmailModel


@admin.register(ContactUsModel)
class ContactUsFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'text']
    search_fields = ('topic',)
    ordering = ['-datetime_created']


@admin.register(NewsEmailModel)
class NewsFormAdmin(admin.ModelAdmin):
    list_display = ['email',]
    search_fields = ('email',)
    ordering = ['-datetime_created']
