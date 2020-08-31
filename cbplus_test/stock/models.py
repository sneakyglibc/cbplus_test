from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class StockReading(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    reference_id = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\d{13}$',
                message=_('The reference_id field has to be 13 digits.'),
                code='invalid_reference_id'
            )
        ]
    )
    expiry_date = models.DateField()
    objects = models.Manager()

