from django.urls import path
from . import views

app_name='member'
urlpatterns = [
    path('login/', views.login,name='login'),
    path('loginChk/', views.loginChk,name='loginChk'),
    path('idChk/', views.idChk,name='idChk'),
    path('logout/', views.logout,name='logout'),
    path('step03/', views.step03,name='step03'),
]
