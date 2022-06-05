from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Fruit
from .serializers import FruitSerializers

# Create your views here.
@api_view(['Get'])
def helloAPI(request):
    return Response("Hello World!")

@api_view(['Get'])
def fruitsList(request):
    totalFruit = Fruit.objects.all()
    serializer = FruitSerializers(totalFruit, many=True)
    return Response(serializer.data)

class FruitInfo(generics.RetrieveAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializers

