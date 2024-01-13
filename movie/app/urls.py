from django.urls import path, include
from app.views import IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',IndexView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)