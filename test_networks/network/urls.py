from django.urls import re_path, path
from network import views

app_name = 'network'

urlpatterns = [
    path(r'device/<int:pk>', views.DeviceRetrieveAPIView.as_view(), name='device'),
    re_path(r'device/?$', views.DeviceAPIView.as_view(), name='devices'),
    path(r'device-type/<int:pk>', views.DeviceTypeRetrieveAPIView.as_view(), name='device_type'),
    re_path(r'device-type/?$', views.DeviceTypeAPIView.as_view(), name='device_types'),
    path(r'tech-place/<int:pk>', views.TechPlaceRetrieveAPIView.as_view(), name='tech_place'),
    re_path(r'tech-place/?$', views.TechPlaceAPIView.as_view(), name='tech_places'),    
]