# Generated by Django 4.0.4 on 2022-04-24 16:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_remove_room_name_remove_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
        ),
    ]
