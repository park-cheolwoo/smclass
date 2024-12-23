from django.urls import path
from . import views

app_name = "Admin"
# Django admin과 혼용하지 않기 위해 대문자 사용
urlpatterns = [
    path("Adminlogin/", views.Adminlogin, name="Adminlogin"),
]
