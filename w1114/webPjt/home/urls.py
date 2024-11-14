from django.urls import path,include
from . import views
### 메인 URL ###
app_name=''
urlpatterns = [
    path("", views.index, name="index"),
]
