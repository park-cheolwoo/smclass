from django.urls import path
from . import views

app_name = "Brand"
urlpatterns = [
    path('',views.brand,name='brand')
]

