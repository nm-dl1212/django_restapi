from rest_framework import serializers
from .models import Bread


class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = ['name', 'price', 'description', 'review', 'priceWithTax'] # GETしたときに渡されるカラムを定義
        read_only_fields = ['created_at', 'updated_at']  # 読み取り専用フィールドとして追加

        