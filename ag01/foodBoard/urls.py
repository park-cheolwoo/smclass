from django.urls import path
from . import views

app_name = "foodBoard"
urlpatterns = [
    path('foodList/', views.foodList, name="foodList"),
    path('foodView/1/', views.foodView, name="foodView"),
    path('foodFind/', views.foodFind, name="foodFind"),
]

