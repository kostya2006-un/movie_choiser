import random
from rest_framework.response import Response
from rest_framework.views import APIView
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


class RandomFilmView(APIView):
    def get(self,*args,**kwargs):
        all_films = Movie.objects.all()
        random_film = random.choice(all_films)
        serializer = MovieSerializer(random_film,many=False)
        return Response(serializer.data)

