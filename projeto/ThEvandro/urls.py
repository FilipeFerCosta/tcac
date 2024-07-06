from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ThEvandro.home.urls")),
    path("login/", include("ThEvandro.login.urls")),
    path("cadastro/", include("ThEvandro.cadastro.urls")),
    path("requerimentos/", include("ThEvandro.requests.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
