# Generated by Django 4.2.7 on 2023-11-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='short_description'),
        ),
    ]
