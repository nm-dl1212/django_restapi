from django.db import models


class Bread(models.Model):

    # ユーザーに入力させる項目
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    
    REVIEW_SET = (
            ("Good", "うまい"),
            ("Soso", "そこそこ"),
            ("Bad", "まずい"),
    )
    review = models.CharField(choices=REVIEW_SET, max_length=8)
    
    # 自動追加される項目
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 計算式を追加
    @property
    def priceWithTax(self):
        return int(self.price * 1.1)
    
    def __str__(self):
        return self.name