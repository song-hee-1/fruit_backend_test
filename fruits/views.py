from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Info
from .serializers import InfoSerializer
from rest_framework import generics


# Create your views here.

@api_view(['Get'])
def helloAPI(request):
    return Response("Hello World!")


@api_view(['Get'])
def fruitsInfoList(request):
    total_fruits_info = Info.objects.all()
    serializer = InfoSerializer(total_fruits_info, many=True)
    return Response(serializer.data)


class FruitInfo(generics.RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
