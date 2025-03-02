import django_filters
from .models import Flight


class FlightFilter(django_filters.FilterSet):
    departure = django_filters.CharFilter(field_name='departure', lookup_expr='icontains')
    destination = django_filters.CharFilter(field_name='destination', lookup_expr='icontains')
    departure_time = django_filters.DateTimeFilter(field_name='departure_time', lookup_expr='gte',input_formats=['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y'])
    arrival_time = django_filters.DateTimeFilter(field_name='arrival_time', lookup_expr='lte',input_formats=['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y'])

    class Meta:
      model = Flight
      fields = ['departure', 'destination', 'departure_time', 'arrival_time']
