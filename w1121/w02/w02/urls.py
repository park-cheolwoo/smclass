from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("board/", include("board.urls")),
    path("member/", include("member.urls")),
    path("", include("home.urls")),
]
