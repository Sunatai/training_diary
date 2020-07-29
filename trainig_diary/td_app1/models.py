from django.db import models

# Create your models here.

BODY_PART = (('warning','胸'),('primary','背中'),('success','足'))

class TrainingDiaryModel(models.Model):
    body_part = models.CharField( #部位
        max_length = 100,
        choices = BODY_PART
    )
    train_name = models.CharField(max_length=100) #種目名
    weight = models.IntegerField() #重さ
    raise_times = models.IntegerField() #回数
    set_times = models.IntegerField() #セット数
    date = models.DateField() #日付
    memo = models.TextField(blank=True, null=True, default='') #メモ
    author = models.CharField(max_length=100, null=True, default='')
    def __str__(self):
        return self.body_part
