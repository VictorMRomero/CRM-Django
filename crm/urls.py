from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path   
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('inicio/', views.index, name="index"),
    path('nuevocliente/', views.nuevocliente, name="nuevocliente"),
    path('editarcliente/<int:idcliente>', views.editarcliente, name="editarcliente"),
    
]