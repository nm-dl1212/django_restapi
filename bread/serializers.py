from rest_framework import serializers
from .models import Bread


class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = ['name', 'price', 'description', 'review', 'priceWithTax'] # GET時に渡す項目
        read_only_fields = ['created_at', 'updated_at']  # 読み取り専用

        