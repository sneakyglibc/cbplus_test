from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import RegexValidator
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _


class StockReading(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
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
    last = models.BooleanField(default=True)
    objects = models.Manager()

    class Meta:
        constraints = [models.constraints.UniqueConstraint(
            fields=['reference_id', 'last'],
            condition=models.Q(last=True),
            name='unique_reference_id_last'
        )]

    def save(self, *args, **kwargs):
        self.full_clean()
        with transaction.atomic():
            if not self.pk:
                try:
                    last_stock_reading = StockReading.objects.get(
                        reference_id=self.reference_id,
                        last=True
                    )
                    last_stock_reading.last = False
                    last_stock_reading.save()
                except ObjectDoesNotExist:
                    pass
            super(StockReading, self).save(*args, **kwargs)
