from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImgDetectViewSet

router = DefaultRouter()
router.register('imgDetect', ImgDetectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]