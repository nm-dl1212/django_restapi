from django.contrib import admin

# Register your models here.
from .models import Product   # 追加

admin.site.register(Product)  # 追加