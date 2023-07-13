from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',views.welcome, name="welcome"),
    path('loginview/',views.loginview, name="loginview"),
    path('uploaddata/', views.uploaddata, name="uploaddata")
]
