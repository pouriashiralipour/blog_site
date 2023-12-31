# Generated by Django 4.2.7 on 2023-11-07 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_article_description_article_description_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('text', models.TextField(verbose_name='text')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='datetime_created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='datetime_modified')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.article', verbose_name='article')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ['-datetime_created'],
            },
        ),
    ]
