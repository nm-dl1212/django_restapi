# Create your views here.
from rest_framework import viewsets
from .models import ImgDetect
from .serializers import ImgDetectSerializer


class ImgDetectViewSet(viewsets.ModelViewSet):

    queryset = ImgDetect.objects.all()
    serializer_class = ImgDetectSerializer