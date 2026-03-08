import django_filters
from .models import ElectronicsNetwork


class ElectronicsNetworkFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='iexact')  # Фильтр по стране (регистронезависимо)
    city = django_filters.CharFilter(lookup_expr='icontains')
    level = django_filters.NumberFilter()

    class Meta:
        model = ElectronicsNetwork
        fields = ['country', 'city', 'level']