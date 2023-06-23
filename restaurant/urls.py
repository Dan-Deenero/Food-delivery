from django.contrib import admin
from django.urls import path, include
from .views import viewDish

urlpatterns = [
    path('view-dish/', viewDish, name='view-dish'),
]