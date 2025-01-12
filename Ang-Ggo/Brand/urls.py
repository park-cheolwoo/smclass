from django.urls import path
from . import views

app_name = "Brand"
urlpatterns = [
    path('',views.brand,name='brand'),
    path('mypage/update/',views.update,name='update'),
    path('mypage/rvwCheck/',views.rvwCheck,name='rvwCheck'),
    path('mypage/resCheck/',views.resCheck,name='resCheck'),
    path('mypage/starCheck/',views.starCheck,name='starCheck'),
    path('mypage/boardCheck/',views.boardCheck,name='boardCheck'),
]

