from django.urls import path
from . import views

app_name = 'adtest'
urlpatterns = [
    path('login/', views.login, name='login'),   # gps테스트
]

