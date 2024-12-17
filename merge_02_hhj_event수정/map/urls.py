from django.urls import path, include
from . import views

app_name = 'map'
urlpatterns = [
    path('mview/', views.mview, name='mview'),
    path('success/', views.success, name='success'),
    path('test4/', views.test4, name='test4'),
    path('test5/', views.test5, name='test5'),
    path('test6/', views.test6, name='test6'),
    path('test7/', views.test7, name='test7'),
    path('test8/', views.test8, name='test8'),
    path('test9/', views.test9, name='test9'),
    path('weather/', views.weather, name='weather')
]

