
from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    # 로그인/로그아웃
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    # 회원정보관련
    path('mlist/',views.mlist,name='mlist'),
    path('mwrite/',views.mwrite,name='mwrite'),
    path('mview/<str:id>/',views.mview,name='mview'),
    path('mupdate/<str:id>/',views.mupdate,name='mupdate'),
    path('mdelete/<str:id>/',views.mdelete,name='mdelete'),
]
