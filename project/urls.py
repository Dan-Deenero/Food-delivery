from django.contrib import admin
from django.urls import path, include
from .views import home, update_profile, contact, dishes, cart, menu

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('dishes/', dishes, name='dishes'),
    path('menu/', menu, name='menu'),
    path('cart/', cart, name='cart'),
    path('update-profile/', update_profile, name='update-profile'),
]