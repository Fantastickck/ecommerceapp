# Generated by Django 4.0.4 on 2022-04-24 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
        migrations.RemoveField(
            model_name='room',
            name='slug',
        ),
    ]
