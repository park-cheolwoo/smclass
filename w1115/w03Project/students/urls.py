from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path("write/", views.write, name="write"),
    path("list/", views.list, name="list"),
]
