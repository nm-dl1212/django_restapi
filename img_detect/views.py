from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import ImgDetect
from .serializers import ImgDetectSerializer


class ImgDetectViewSet(viewsets.ModelViewSet):

    queryset = ImgDetect.objects.all()
    serializer_class = ImgDetectSerializer