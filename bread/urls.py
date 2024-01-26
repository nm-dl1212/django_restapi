from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BreadViewSet


router = DefaultRouter()
router.register('bread', BreadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]