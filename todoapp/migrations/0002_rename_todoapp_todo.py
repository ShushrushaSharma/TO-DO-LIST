# Generated by Django 4.2.3 on 2023-08-01 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todoapp',
            new_name='Todo',
        ),
    ]
