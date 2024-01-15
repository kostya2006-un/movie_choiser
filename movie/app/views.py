from app.serializers import MovieSerializer
from rest_framework import viewsets
from app.models import Movie


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
