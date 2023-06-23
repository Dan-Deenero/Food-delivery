from django.contrib import admin
from django.urls import path, include
from .views import login, register, forgetPassword

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forgetPassword/', forgetPassword, name='forgetPassword'),
]