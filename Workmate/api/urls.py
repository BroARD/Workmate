from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kittens.views import KittenViewSet, BreedViewSet, KittenRatingListAPIView

app_name = 'api'

router = DefaultRouter()
router.register(r'kittens', KittenViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'kittens/(?P<kitten_id>[^/.]+)/ratings', KittenRatingListAPIView, basename='kitten-ratings')

urlpatterns = [
    path('', include(router.urls)),
]
