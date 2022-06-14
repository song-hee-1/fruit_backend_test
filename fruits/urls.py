from django.urls import path, include
from .views import FruitsInfoList, FruitInfo

urlpatterns = [
    path("", FruitsInfoList.as_view()),
    path("<int:pk>/", FruitInfo.as_view()),
]