from django.urls import path, include
from . import views

app_name = "account"

urlpatterns = [
    path('', views.default),
    path('login/', views.login, name='login'),
    path('register/', views.register),
]
