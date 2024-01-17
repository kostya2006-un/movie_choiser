from django.urls import path, include
from rest_framework import routers
from app.views import MovieViewSet,RandomFilmView


router = routers.SimpleRouter()
router.register(r'movie',MovieViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/random_film/',RandomFilmView.as_view(),name = 'random-film')
]