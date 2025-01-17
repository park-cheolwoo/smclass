from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('mlist/', views.mlist, name="mlist"),
    path('login/', views.login, name="login"),
    path('login2/', views.login2, name="login2"),
    path('product/', views.product, name="product"),
    path('m2/', views.m2, name="m2"),
]
