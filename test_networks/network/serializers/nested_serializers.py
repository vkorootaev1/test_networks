from rest_framework import serializers
from network import models


class DeviceTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.DeviceType
        fields = '__all__'
        

class TechPlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.TechPlace
        fields = '__all__'