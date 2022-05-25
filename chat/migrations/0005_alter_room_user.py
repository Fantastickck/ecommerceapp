# Generated by Django 4.0.4 on 2022-05-13 08:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_alter_message_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='rooms', to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
        ),
    ]
