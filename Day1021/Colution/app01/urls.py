from django.contrib import admin
from django.urls import path, re_path, include
from app01 import views
urlpatterns = [
    path('index/', views.app01index),
]
