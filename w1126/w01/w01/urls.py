from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('member/', include('member.urls')),
    path('board/', include('board.urls')),
]


# media 문서를 찾도록 하는 함수
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
