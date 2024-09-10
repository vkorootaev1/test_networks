from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from network.models import Device
from network.serializers.serializers import DeviceSerializer


class DeviceAPIView(APIView):
    
    # 1
    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
      
    def get(self, request, pk=None):
        
        many=False
        
        # 3
        if pk is not None:
            data = get_object_or_404(Device, pk=pk)
        # 2.1
        elif request.data:
            data = get_object_or_404(Device, **request.data)
        # 2.2
        else:
            many = True
            data = Device.objects.all()
            
        serializer = DeviceSerializer(data, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)