from django.urls import path, include
from . import views

app_name = "foodBoard"
urlpatterns = [
    path('foodList/', views.foodList, name="foodList"),
    path('foodWrite/', views.foodWrite, name="foodWrite"),
    path('foodView/<int:bNo>/', views.foodView, name="foodView"),
    path('foodFind/', views.foodFind, name="foodFind"),
    path('foodRes/<int:bNo>/', views.foodRes, name="foodRes"),
]

