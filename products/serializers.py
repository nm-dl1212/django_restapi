from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'review', 'priceWithTax'] # GETしたときに渡されるカラムを定義
        read_only_fields = ['created_at', 'updated_at']  # 読み取り専用フィールドとして追加

        