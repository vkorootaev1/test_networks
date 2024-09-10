from rest_framework import serializers
from network.models import Device, DeviceType, TechPlace
from network.serializers import nested_serializers


class DeviceSerializer(serializers.ModelSerializer):
    type = nested_serializers.DeviceTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(queryset=DeviceType.objects.all(), source='type', write_only=True)
    tech_place = nested_serializers.TechPlaceSerializer(read_only=True)
    tech_place_id = serializers.PrimaryKeyRelatedField(queryset=TechPlace.objects.all(), source='tech_place', write_only=True)

    class Meta:
        model = Device
        fields = ['id', 'name', 'parent', 'type', 'type_id', 'date_add', 'tech_place', 'tech_place_id']

    def create(self, validated_data):
        obj, _ = Device.objects.get_or_create(**validated_data)
        return obj
        