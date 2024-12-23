from django.urls import path
from . import views


app_name = 'board'
urlpatterns = [
    path("blist/", views.blist, name="blist"),
    path("bwrite/", views.bwrite, name="bwrite"),
    path("bview/<int:bno>/", views.bview, name="bview"),
    path("bmodify/<int:bno>/", views.bmodify, name="bmodify"),
    path("bdelete/<int:bno>/", views.bdelete, name="bdelete"),
    path("breply/<int:bno>/", views.breply, name="breply"),
]
