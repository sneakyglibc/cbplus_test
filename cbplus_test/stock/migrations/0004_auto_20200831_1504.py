# Generated by Django 3.1 on 2020-08-31 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20200831_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockreading',
            old_name='last_update',
            new_name='last_update_date',
        ),
    ]
