import django_filters
from core import models


class WeatherFilter(django_filters.FilterSet):
    locality = django_filters.CharFilter(lookup_expr='iexact')
    now_dt = django_filters.DateTimeFilter(lookup_expr='lte')

    class Meta:
        model = models.Weather
        fields = ['locality', 'now_dt']



