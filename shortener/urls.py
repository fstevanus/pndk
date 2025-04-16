from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShortenedURLViewSet

router = DefaultRouter()
router.register(r'urls', ShortenedURLViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
