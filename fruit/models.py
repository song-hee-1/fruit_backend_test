from django.db import models


# Create your models here.
class Fruit(models.Model):
    fid = models.IntegerField()
    name = models.CharField(max_length=10)
    season = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'images/', blank=True, null=True)
