from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),    # h
    path('foodBoard/', include('foodBoard.urls')),    # c
    path('Brand/',include('Brand.urls')),    # c
    path('map/', include('map.urls')),    # w
    path('board/', include('board.urls')),    # w
    path('comment/', include('comment.urls')),    # w
    path('member/', include('member.urls')),    # s
]


# media 연결
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)