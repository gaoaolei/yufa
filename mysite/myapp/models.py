from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class UserData(models.Model):
    nickname = models.CharField(default='leiyu',max_length=32)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

