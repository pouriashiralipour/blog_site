# Generated by Django 4.2.7 on 2023-11-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_contactusmodel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
    ]
