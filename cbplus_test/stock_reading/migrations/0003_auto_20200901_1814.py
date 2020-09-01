# Generated by Django 3.1 on 2020-09-01 18:14

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stock_reading', '0002_remove_stockreading_last_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockreading',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='stockreading',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='stockreading',
            name='reference_id',
            field=models.CharField(db_index=True, max_length=13, validators=[django.core.validators.RegexValidator(code='invalid_reference_id', message='The reference_id field has to be 13 digits.', regex='^\\d{13}$')]),
        ),
    ]