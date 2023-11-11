from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

from .models import Article, Category, Comments


@admin.register(Article)
class ArticleAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'author', 'cover_img', 'status', 'jalali_publish']
    list_filter = ('publish', 'status',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']


@admin.register(Category)
class ArticleCategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'active', 'jalali_publish']
    list_filter = ('active',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-datetime_created']


@admin.register(Comments)
class CommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'is_active', 'text', 'jalali_publish']
    list_filter = ('is_active',)
    search_fields = ('text',)
    ordering = ['-datetime_created']


@admin.register(Category)
class TagsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['tag', 'active', 'jalali_publish']
    list_filter = ('active',)
    search_fields = ('tag',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-datetime_created']
