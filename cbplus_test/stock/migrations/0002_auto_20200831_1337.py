# Generated by Django 3.1 on 2020-08-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='stockreading',
            constraint=models.UniqueConstraint(condition=models.Q(last=True), fields=('reference_id', 'last'), name='unique_reference_id_last'),
        ),
    ]
