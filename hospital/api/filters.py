import django_filters as filters
from .models import Medic


class MedicFilters(filters.FilterSet):
    last_name = filters.CharFilter(field_name='last_name')


    class Meta:
        model = Medic
        fields = {
            'last_name':['exact','contains'],
            'first_name':['exact'],
            'spetiality':['exact',]
        }