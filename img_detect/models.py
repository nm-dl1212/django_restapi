from django.db import models
from .detect import detect

class ImgDetect(models.Model):

    # 入力するカラム
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=500)
    
    # 自動追加されるカラム
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 空白のカラム
    inference_label = models.CharField(max_length=255, blank=True, null=True,  editable=False)
    
    def save(self, *args, **kwargs):
        # オーバーライドして保存前に推論ラベルを設定
        if not self.inference_label:
            self.inference_label = detect(self.path)
        super().save(*args, **kwargs)

    @property
    def inference_image(self):
        return "画像へのパス"

    def __str__(self):
        return self.name