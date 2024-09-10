from django.contrib import admin
from network.models import *

@admin.register(Device, DeviceType, TechPlace)
class NetworkAdmin(admin.ModelAdmin):
    pass 
