# Generated by Django 4.0.5 on 2022-06-29 10:43

import authy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0002_profile_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=authy.models.user_directory_path, verbose_name='Picture'),
        ),
    ]