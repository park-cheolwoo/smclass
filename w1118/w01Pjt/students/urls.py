from django.urls import path
from . import views

app_name = 'students' # name:url시 사용
urlpatterns = [
    path("list/", views.list, name="list"),  # 학생 리스트 페이지
    path("write/", views.write, name="write"),  # 학생 입력/저장 페이지
    path("<str:name>/view/", views.view, name="view"),  # 학생 상세페이지 # 변수:name
    path("<str:name>/modify/", views.modify, name="modify"),  # 학생 수정페이지1 - url
    path("modify2/", views.modify2, name="modify2"),  # 학생 수정페이지2 - 파라미터
    path("<str:name>/modify3", views.modify3, name="modify3"),  # 학생 수정페이지3 - AppName
    path("<str:name>/delete", views.delete, name="delete"),  # 학생 삭제 페이지
]
