import django_filters
from .models import *

class foodItemFilter(django_filters.FilterSet):
    class Meta:
        model = foodItem
        fields = ['name']