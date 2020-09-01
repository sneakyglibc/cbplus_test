from rest_framework import serializers

from .. import models


class StockReadingSerializer(serializers.ModelSerializer):
    creation_date = serializers.CharField(read_only=True)

    class Meta:
        model = models.StockReading
        fields = ['creation_date', 'reference_id', 'expiry_date', 'uuid']
