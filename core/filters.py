import django_filters
from . import models

class Animal(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Название', lookup_expr='icontains')
    population = django_filters.NumberFilter(label='Популяция от', lookup_expr='gt', field_name='population')

    class Meta:
        model = models.Animal
        exclude = ('information',)