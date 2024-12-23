from django.urls import path
from . import views

app_name = "students"  # app_name 설정
urlpatterns = [
    # url링크 ,views함수호출 ,name링크
    path("write/", views.write, name="write"),
    path("list/", views.list, name="list"),
    path("search/", views.search, name="search"),
    path("view/<str:name>", views.view, name="view"), # app_name 형태
    path("update/", views.update, name="update"),  # 파라미터 형태
    # path('update/<str:name>/', views.update,name='update'),
    path("delete/<str:name>/", views.delete, name="delete"),  # url 형태
]
