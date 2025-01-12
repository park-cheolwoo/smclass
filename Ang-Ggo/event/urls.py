from django.urls import path, include
from . import views

app_name = 'event'
urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),
    path('apply/', views.apply, name='apply'),
    path('luckyDraw/', views.luckyDraw, name='luckyDraw'),
    path('coupon/', views.coupon, name='coupon'),
    path('point/', views.point, name='point'),

]

