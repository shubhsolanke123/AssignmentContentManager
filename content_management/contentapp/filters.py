from django_filters import restframework as filters
from .models import Content

class ContentFilters(filters.Filterset):

    categories= filters.CharFilter(field_name='name',Lookup_expr='icontains')
    title= filters.CharFilter(field_name='name',Lookup_expr='icontains')


    class Meta:
        model=Content
        fields= ('categories','title')