from django.db import models

# Create your models here.
class Test(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
