from django.urls import path
from .views import fruitsList, FruitInfo

urlpatterns = [
    path("", fruitsList),
    path("<int:pk>/", FruitInfo.as_view()),
]