from django.urls import path
from . import views

app_name = '' 
urlpatterns = [
    path('', views.index, name='index') # 메인 페이지 : index,main,default
]
