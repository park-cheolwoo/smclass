from django.urls import path
from . import views

app_name='member'
urlpatterns = [
    path("login/", views.login, name="login"),
    path("loginChk/", views.loginChk, name="loginChk"),
    path("join01/", views.join01, name="join01"),
    path("join02/", views.join02, name="join02"),
    path("idChk/", views.idChk, name="idChk"),
]
