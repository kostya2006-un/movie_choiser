from django_filters import rest_framework as filters

from app.models import Movie


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MovieFilters(filters.FilterSet):
    genres = CharFilterInFilter(field_name='genres__name',lookup_expr='in')
    countries = CharFilterInFilter(field_name='countries__name', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Movie
        fields = ["genres","year","countries"]

