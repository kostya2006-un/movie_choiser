from rest_framework import serializers
from app.models import Movie,Genre,Country


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    countries = CountrySerializer(many=True)

    class Meta:
        model = Movie
        fields = ("genres","countries","name","year","img")
