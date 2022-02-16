from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.registerPage, name='register'),
    path('register/', views.userRegister, name='register'),
    path('login/', views.loginView, name='login'),
    path('loginuser/', views.loginUser, name='loginuser'),
]