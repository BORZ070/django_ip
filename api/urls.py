from django.urls import path, include
from api.views import (IpModelViewSet, GetIpModelViewSet, PostIpModelViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('history', IpModelViewSet, basename='history')
router.register('get-ip', GetIpModelViewSet, basename='get-ip')
router.register('post-ip', PostIpModelViewSet, basename='post-ip')


urlpatterns = [
    path('', include(router.urls))
    ]
