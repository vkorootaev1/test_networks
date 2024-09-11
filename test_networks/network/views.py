from django.shortcuts import get_object_or_404
from django.db.models import Model
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from network.models import Device, DeviceType, TechPlace
from network.serializers import DeviceSerializer, DeviceTypeSerializer, TechPlaceSerializer


class AbstractAPiView(APIView):
    """ Абстрактный класс с атрибутами модели и сериализатора  """
    
    model = None
    serializer = None
    
    def get_model_class(self):
        assert self.model is not None, (
            "'%s' append `model` attribute "
            % self.__class__.__name__
        )
        assert not isinstance(self.model, Model), (
            "'%s' the `model` attribute should belong to the `django.db.models.Model` "
            % self.__class__.__name__
        )
        return self.model
    
    def get_serializer_class(self):
        assert self.serializer is not None, (
            "'%s' append `serializer` attribute "
            % self.__class__.__name__
        )
        assert not isinstance(self.model, Serializer), (
            "'%s' the `serializer` attribute should belong to the `rest_framework.serializers.Serializer` "
            % self.__class__.__name__
        )
        return self.serializer 
    


class AbstractPluralApiView(AbstractAPiView):
    """ Абстрактный класс для множества записей (без указания в url <pk>)  """
    
     # 1
    def post(self, request):
        serializer_class = self.get_serializer_class()
        model_class = self.get_model_class()
        
        serializer = serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            many = False
            status_ = status.HTTP_200_OK
            
            qs = model_class.objects.filter(**serializer.validated_data)
            
            # Совпадений нет - создаем новый объект
            if not len(qs):
                data = model_class.objects.create(**serializer.validated_data)
                status_ = status.HTTP_201_CREATED
            # Одиночное совпадение
            elif len(qs) == 1:
                data = qs[0]
            # Множественное совпадение
            else:
                many = True
                data = qs
            serializer = serializer_class(data, many=many)
            return Response(serializer.data, status=status_)   
    
    # 2  
    def get(self, request):      
        serializer_class = self.get_serializer_class()
        model_class = self.get_model_class() 
            
        many = True
        
        # 2.1 (Если передано тело запроса)
        if request.data:           
            qs = model_class.objects.filter(**request.data)    
                  
            # 2.1 Не найдено совпадений (404)
            if len(qs) == 0:
                return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
            # Одиночное совпадение    
            elif len(qs) == 1:
                many = False
                data = qs[0]
            # Множественное совпадение
            else:
                data = qs    
        # 2.2 (Если не передано тело запроса)
        else:
            data = model_class.objects.all()
            
        serializer = serializer_class(data, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AbstractSingularAPIView(AbstractAPiView):
    """ Абстрактный класс для одиночных записей (c указанием в url <pk>)  """
    
    # 3
    def get(self, request, pk=None):       
        serializer_class = self.get_serializer_class()
        model_class = self.get_model_class()
        
        obj = get_object_or_404(model_class, pk=pk)
        serializer = serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    
class DeviceAPIView(AbstractPluralApiView):
    """ Представление для устройства """

    model = Device
    serializer = DeviceSerializer    
    

class DeviceRetrieveAPIView(AbstractSingularAPIView):
    """ Представление для конкретного устройства """
    
    model = Device
    serializer = DeviceSerializer    
        
 
class DeviceTypeAPIView(AbstractPluralApiView):
    """ Представление для типа устройства """ 
    
    model = DeviceType
    serializer = DeviceTypeSerializer     
    

class DeviceTypeRetrieveAPIView(AbstractSingularAPIView):
    """ Представление для конкретного типа устройства """
    
    model = DeviceType
    serializer = DeviceTypeSerializer        
        
 
class TechPlaceAPIView(AbstractPluralApiView):
    """ Представление для меcтонахождения устройства """

    model = TechPlace    
    serializer = TechPlaceSerializer  
    

class TechPlaceRetrieveAPIView(AbstractSingularAPIView):
    """ Представление для меcтонахождения устройства """
    
    model = TechPlace
    serializer = TechPlaceSerializer       