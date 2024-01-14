from django.db import models

# Create your models here.
# 以下を追加
class ImgDetect(models.Model):

    # 入力するカラム
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=500)
    
    # 自動追加されるカラム
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 計算式を追加
    @property
    def inference_label(self):
        return "ラベル"
    
    @property
    def inference_image(self):
        return "画像へのパス"
    
    def __str__(self):
        return self.name