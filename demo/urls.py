# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from demo.views import CityViewSet, RoomViewSet, HostViewSet, PingHostAPIView, ChangePwView, HostStatViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'hoststats', HostStatViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('ping/', PingHostAPIView.as_view(), name='ping-host'),
    path('change/', ChangePwView.as_view(), name='change-pwd'),
]