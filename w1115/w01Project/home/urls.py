from django.urls import path
from . import views

app_name = '' # app 이름 : 이름으로 접근
urlpatterns = [
    # views.py 연결 - 함수 호출, app 함수 이름
    path("", views.index,name='index')
]
