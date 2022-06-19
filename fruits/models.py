from django.db import models


# Create your models here.
class Info(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=10)
    season = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=100, blank=True, null=True)
