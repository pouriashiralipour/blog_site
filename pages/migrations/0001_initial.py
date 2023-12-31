# Generated by Django 4.2.7 on 2023-11-07 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('topic', models.CharField(max_length=300, verbose_name='topic')),
                ('text', models.TextField(verbose_name='text')),
            ],
        ),
    ]
