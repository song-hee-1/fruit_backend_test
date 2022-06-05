from rest_framework import serializers
from .models import Fruit


class FruitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ('pk', 'name', 'season', 'description', 'image')
