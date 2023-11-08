from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

from .models import ContactUsModel, NewsEmailModel


@admin.register(ContactUsModel)
class ContactUsFormAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'topic', 'text']
    search_fields = ('topic',)
    ordering = ['-datetime_created']


@admin.register(NewsEmailModel)
class NewsFormAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['email',]
    search_fields = ('email',)
    ordering = ['-datetime_created']
