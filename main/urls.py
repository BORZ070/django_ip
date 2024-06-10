from django.contrib import admin
from django.urls import path, include

from main.views import main_views, error_views

urlpatterns = [
    path('', main_views, name='main'),
    path('error/', error_views, name='error')
]