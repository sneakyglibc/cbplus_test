import django_filters.rest_framework

from rest_framework import viewsets, mixins

from .serializers import StockReadingSerializer
from ..models import StockReading


class ProjectFilter(django_filters.FilterSet):
    reference_id = django_filters.CharFilter(lookup_expr='icontains')
    last = django_filters.BooleanFilter(method='filter_last')
    cursor = django_filters.UUIDFilter(method='filter_cursor')

    def filter_last(self, queryset, name, value):
        if value is True:
            queryset = queryset.distinct('reference_id')
            return queryset
        elif value is False:
            queryset = queryset.difference(queryset.distinct('reference_id')).order_by('reference_id', '-creation_date')
            return queryset
        return queryset

    def filter_cursor(self, queryset, name, value):
        stock_reading = StockReading.objects.filter(uuid=value)
        if not stock_reading:
            return []
        return queryset.filter(creation_date__gt=stock_reading.first().creation_date)

    class Meta:
        model = StockReading
        fields = ('reference_id', 'last',)


class StockReadingViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = StockReadingSerializer
    queryset = StockReading.objects.all().order_by('reference_id', '-creation_date')
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ProjectFilter
