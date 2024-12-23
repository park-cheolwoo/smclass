from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path("write/", views.write, name="write"),
    path("list/", views.list, name="list"),
    path("view/<str:name>/", views.view, name="view"),
    path("update/<str:name>/", views.update, name="update"),
    path("delete/<str:name>/", views.delete, name="delete"),
]
