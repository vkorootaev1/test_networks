from rest_framework import serializers
from network.models import Device, DeviceType, TechPlace


class DeviceTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceType
        fields = '__all__'
        

class TechPlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TechPlace
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'

    # def create(self, validated_data):
    #     obj, _ = Device.objects.get_or_create(**validated_data)
    #     return obj
        