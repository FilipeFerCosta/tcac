# In ThEvandro/login/urls.py
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),  # Ensure this line is correct
]
