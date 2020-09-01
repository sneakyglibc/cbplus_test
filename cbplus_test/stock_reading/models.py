import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class StockReading(models.Model):
    creation_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    reference_id = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\d{13}$',
                message=_('The reference_id field has to be 13 digits.'),
                code='invalid_reference_id'
            )
        ],
        db_index=True
    )
    expiry_date = models.DateField()
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True
    )
    objects = models.Manager()
