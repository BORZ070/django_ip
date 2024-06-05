from django.urls import path, include
from api.views import (IpModelViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('history', IpModelViewSet)


urlpatterns = [
    path('', include(router.urls))
    ]