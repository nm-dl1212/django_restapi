# Create your views here.
from rest_framework import viewsets
from .models import Bread
from .serializers import BreadSerializer


class BreadViewSet(viewsets.ModelViewSet):

    queryset = Bread.objects.all()
    serializer_class = BreadSerializer