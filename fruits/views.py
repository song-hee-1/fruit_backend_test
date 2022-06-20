from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Info
from .serializers import InfoSerializer
from rest_framework import generics
from django.shortcuts import render

# Create your views here.

@api_view(['Get'])
def helloAPI(request):
    fruits_info_list = Info.objects.all()
    context = {
        'fruits_info_list' : fruits_info_list
    }
    return render(request, 'fruits/index.html', context)



class FruitsInfoList(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer



class FruitInfo(generics.RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
