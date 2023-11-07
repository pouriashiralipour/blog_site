import random

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    slug = models.SlugField(max_length=200, verbose_name=_('slug'), unique=True, allow_unicode=True)
    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'), )
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))
    active = models.BooleanField(default=True, verbose_name=_('active'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _("categories")
        ordering = ['datetime_created']

    # def get_absolute_url(self):
    #         return reverse('category:category', args=[self.slug])

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', _('Draft')),
        ('p', _('Published')),
    )

    title = models.CharField(max_length=500, verbose_name=_('title'))
    slug = models.SlugField(max_length=500, verbose_name=_('slug'), unique=True, allow_unicode=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('author'))
    category = models.ManyToManyField(Category, verbose_name=_('category'), related_name='article')
    description_1 = RichTextField(verbose_name=_('description_1'), blank=True)
    description_2 = RichTextField(verbose_name=_('description_2'), blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', verbose_name=_('thumbnail'))
    image_1 = models.ImageField(upload_to='images/', verbose_name=_('image_1'), blank=True, null=True)
    image_2 = models.ImageField(upload_to='images/', verbose_name=_('image_2'), blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name=_('status'))
    publish = models.DateTimeField(default=timezone.now, verbose_name=_('publish'))
    offer_article = models.BooleanField(default=False, verbose_name=_('offer_article'))
    hottest_article = models.BooleanField(default=False, verbose_name=_('hottest_article'), blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ['-datetime_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:details_view', args=[self.slug])

    def cover_img(self):
        try:
            return format_html("<img width=60 src='{}'>".format(self.thumbnail.url))
        except:
            return ''

    cover_img.short_description = _('thumbnail')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                             verbose_name=_('user'))
    name = models.CharField(max_length=200, verbose_name=_('name'), related_name='comments')
    email = models.EmailField(verbose_name=_('email'))
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name=_('article'))
    text = models.TextField(verbose_name=_('text'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['-datetime_created']


def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance


def products_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    # print(sender, instance)
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(products_pre_save, sender=Article)


def products_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    # print(args, kwargs)
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(products_post_save, sender=Article)
