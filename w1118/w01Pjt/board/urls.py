from django.urls import path
from . import views

app_name = 'board' # name:url시 사용
urlpatterns = [
    path('list/', views.list, name='list') # 학생 입력 페이지
]
