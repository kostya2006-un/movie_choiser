from django.urls import path, include
from rest_framework import routers
from app.views import MovieViewSet


router = routers.SimpleRouter()
router.register(r'movie',MovieViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
]