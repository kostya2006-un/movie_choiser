from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Genre,Movie,Country
from app.serializers import MovieSerializer


class MovieTestCase(APITestCase):
    def test_get(self):
        genre = Genre.objects.create(name='драма')
        country = Country.objects.create(name='Россия')
        movie = Movie.objects.create(name='test', year=2010, img='')
        movie1 = Movie.objects.create(name='test2', year=2012, img='')

        movie.genres.set([genre])
        movie.countries.set([country])

        url = reverse('movie-list')
        response = self.client.get(url)
        serializer = MovieSerializer([movie,movie1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer, response.data)
        url = '/api/v1/random_film/'


