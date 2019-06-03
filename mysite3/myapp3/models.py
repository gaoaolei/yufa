from django.db import models

# Create your models here.
class userinfo(models.Model):
    name = models.CharField(max_length=32)
    height = models.IntegerField(default=0)
    age = models.IntegerField(default=0)