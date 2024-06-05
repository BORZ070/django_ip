from django.contrib import admin
from django.urls import path, include

from main.views import main_views

urlpatterns = [
    path('', main_views, name='main')
]