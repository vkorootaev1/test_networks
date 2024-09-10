from django.urls import path, include
from network import views

app_name = 'network'

urlpatterns = [
    path(r'device/<uuid:pk>', views.DeviceAPIView.as_view(), name='device'),
    path(r'device', views.DeviceAPIView.as_view(), name='devices')
]