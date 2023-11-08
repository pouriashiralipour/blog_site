from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

from .models import Article, Category, Comments


@admin.register(Article)
class ArticleAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'author', 'cover_img', 'status', 'publish']
    list_filter = ('publish', 'status',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']

    # @admin.display(description='تاریخ انتشار', ordering='publish')
    # def get_created_jalali(self, obj):
    #     return datetime2jalali(obj.publish).strftime('%a, %d %b %Y %H:%M:%S')


@admin.register(Category)
class ArticleCategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'active', 'datetime_created']
    list_filter = ('active',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-datetime_created']


@admin.register(Comments)
class ArticleCommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'is_active', 'text']
    list_filter = ('is_active',)
    search_fields = ('text',)
    ordering = ['-datetime_created']
