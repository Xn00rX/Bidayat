# Generated by Django 4.2.7 on 2023-11-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_profile_image_profile_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]
