from django.contrib import admin
from django.urls import path   
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nuevocliente/', views.nuevocliente, name="nuevocliente"),
    path('editarcliente/<int:idcliente>', views.editarcliente, name="editarcliente") 
]