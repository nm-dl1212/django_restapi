from rest_framework import serializers
from .models import ImgDetect


class ImgDetectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgDetect
        fields = ['name', 'path', 'inference_label', 'inference_image'] # GET時に渡す項目
        read_only_fields = ['created_at', 'updated_at']  # 読み取り専用

        