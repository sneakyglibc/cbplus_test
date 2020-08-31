from rest_framework import serializers

from .. import models


class ModelsSerializer(serializers.ModelSerializer):
    last = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.StockReading
        fields = "__all__"
