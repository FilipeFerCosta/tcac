from django.urls import path
from . import views

app_name = 'cadastro'

urlpatterns = [
    path("", views.Cadastro.as_view(), name="cadastro"),
]
