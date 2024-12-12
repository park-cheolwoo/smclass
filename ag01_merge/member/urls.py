from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    path('mlist/', views.mlist, name='mlist'),
    path('login/', views.login, name="login"),  # 로그인
    path('loginChk/', views.loginChk, name="loginChk"),  # 로그인 확인
    path('logout/', views.logout, name="logout"),  # 로그아웃

    path('join01/', views.join01, name="join01"),  # 회원가입 step01 약관동의
]

