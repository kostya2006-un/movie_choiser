import os
import requests
from app.models import Genre
from app.kinopoisk_api import KP
from app.models import Country,Movie
from django.core.files import File

def kino():
    kinopoisk = KP(token='7e315dd4-e4f0-4e9e-91e2-5f736ca85f6f')
    top500 = kinopoisk.top500()
    i = 0
    for item in top500:
        i += 1

        movie, created = Movie.objects.get_or_create(
            name=item.ru_name,
            year=item.year,
        )

        genre_objects = []
        for genre in item.genres:
            genre_instance, created = Genre.objects.get_or_create(name=genre)
            genre_objects.append(genre_instance[0] if isinstance(genre_instance, tuple) else genre_instance)

        country_objects = []
        for country in item.countries:
            country_instance, created = Country.objects.get_or_create(name=country)
            country_objects.append(country_instance[0] if isinstance(country_instance, tuple) else country_instance)

        movie.genres.add(*genre_objects)
        movie.countries.add(*country_objects)
        movie.save()
        photo_movie(movie, item.poster_preview, '/photo')


def photo_movie(movie, url_photo, download_path):
    response = requests.get(url_photo)

    if response.status_code == 200:
        file_name = f"{movie.name.replace(' ', '_')}.jpg"

        # Save the photo to the folder
        with open(download_path, 'wb') as file:
            file.write(response.content)

        # Save the photo to the model's ImageField
        with open(download_path, 'rb') as file:
            movie.img.save(file_name, File(file), save=True)
            print(f"Фото сделано для {movie.name}")

        os.remove(download_path)
    else:
        print(f"Не удалось скачать фото для фильма {movie.name}")






