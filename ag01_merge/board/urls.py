from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('nboard/', views.nboard, name='nboard'),   # 게시판리스트
    path('bwrite/', views.bwrite, name='bwrite'),   # 게시판 글쓰기
    path('bbview/<int:bno>/', views.bbview, name='bbview'),   # 게시글 상세보기
    path('bdelete/<int:bno>/', views.bdelete, name='bdelete'),   # 게시글 삭제하기
    path('bmodify/<int:bno>/', views.bmodify, name='bmodify'),   # 게시글 수정하기
    path('likes/', views.likes,name="likes"),   # 게시글 좋아요 기능
    path('gps_test/', views.gps_test, name='gps_test'),   # gps테스트
]

