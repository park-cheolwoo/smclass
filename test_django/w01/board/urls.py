from django.urls import path,include
from . import views

app_name = "board"
urlpatterns = [
    # path('blist/', views.blist,name="blist"),
    path("likes/", views.likes, name="likes"),
    path("form/", views.form, name="form"),
    # path('bview/<int:bno>/', views.bview,name="bview"), 
    path("bview/<int:pk>/", views.BoardDetailView.as_view()), # bno가 아닌 pk로 입력해야함 # Model+DetailView
    path("blist/", views.BoardListView.as_view()), # Model+ListView
]
