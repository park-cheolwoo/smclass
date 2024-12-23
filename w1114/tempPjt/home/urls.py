from django.urls import path
from . import views

app_name = ""
urlpatterns = [
    ## url 주소 / views.py 함수명, url 이름
    # http://127.0.0.1:8000/students/reg/
    # students/reg
    path("", views.index, name="index"),
]
