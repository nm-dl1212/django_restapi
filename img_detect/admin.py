from django.contrib import admin

# Register your models here.
from .models import ImgDetect   # 追加

admin.site.register(ImgDetect)  # 追加