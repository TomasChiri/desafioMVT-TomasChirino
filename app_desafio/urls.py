from django.contrib import admin
from django.urls import path
from app_desafio.views import listar_familiares

urlpatterns = [
    path('familia/', listar_familiares)
]