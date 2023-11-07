from django.contrib import admin

from .models import Article, Category, Comments


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'cover_img', 'status', 'publish', 'datetime_created', 'datetime_modified']
    list_filter = ('publish', 'status',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']


@admin.register(Category)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'datetime_created']
    list_filter = ('active',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-datetime_created']


@admin.register(Comments)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'text']
    list_filter = ('is_active',)
    search_fields = ('text',)
    ordering = ['-datetime_created']
