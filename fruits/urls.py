from django.urls import path, include
from .views import fruitsInfoList, FruitInfo

urlpatterns = [
    path("", fruitsInfoList),
    path("<int:pk>/", FruitInfo.as_view()),
]