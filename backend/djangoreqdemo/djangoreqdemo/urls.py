from django.contrib import admin
from django.urls import path, include
import rest_framework
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('auth/', include('users.urls')),
    path('nutrient/', include('nutrient.urls')),
]
