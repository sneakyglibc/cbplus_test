# Generated by Django 3.1 on 2020-09-01 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_reading', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockreading',
            name='last_update_date',
        ),
    ]
