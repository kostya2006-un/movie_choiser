from app.serializers import MovieSerializer
from rest_framework import viewsets
from app.models import Movie
from django_filters import rest_framework as filters
from app.service import MovieFilters


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = MovieFilters
