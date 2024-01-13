from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    genres = models.ManyToManyField(Genre)
    countries = models.ManyToManyField(Country)
    name = models.CharField(max_length=255,default=None)
    year = models.PositiveIntegerField(default=None)
    img = models.ImageField(upload_to='movie_img',default=None)

    def __str__(self):
        return self.name