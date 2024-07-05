from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ThEvandro.home.urls")),
    path("login/", include("ThEvandro.login.urls")),
    path("cadastro/", include("ThEvandro.cadastro.urls")),
    path("requerimentos/", include("ThEvandro.requests.urls")),
]
