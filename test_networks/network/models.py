from django.db import models
import uuid


class AbstractUUIDModel(models.Model):
    """ Абстрактная модель с первичным ключом в формате <UUID> """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Идентификатор', editable=False)
    
    class Meta:
        abstract = True


class Device(AbstractUUIDModel):
    """ Описание устройства """
    
    name = models.CharField(max_length=150, verbose_name='Наименование устройства')
    parent = models.ForeignKey('self', verbose_name='Родительское устройство', on_delete=models.PROTECT, null=True, blank=True, related_name='children', db_column='parent_id')
    type = models.ForeignKey('DeviceType', verbose_name='Тип устройства', on_delete=models.PROTECT, db_column='device_type_id')
    date_add = models.DateTimeField(verbose_name='Дата добавления устройства')
    tech_place = models.ForeignKey('TechPlace', verbose_name='Местонахождение устройства', on_delete=models.PROTECT, db_column='tech_place_id')
    
    def __str__(self):
        return f'{self.name}' 
    
    class Meta:
        db_table = 'device'
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'       
    
    
class DeviceType(AbstractUUIDModel):
    """ Описание типа устройства """
    
    name = models.CharField(max_length=150, verbose_name='Наименование типа устройства')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = 'device_type'
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Типы устройств'
        
    
class TechPlace(AbstractUUIDModel):
    """ Описание местонахождения устройства """
    
    address = models.TextField(verbose_name='Адрес местонахождение устройства', db_column='address')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Широта местонахождения устройства')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота местонахождения устройства')
    
    def __str__(self):
        return f'{self.address} ({self.latitude}, {self.longitude})'
    
    class Meta:
        db_table = 'tech_place'
        verbose_name = 'Местонахождение устройства'
        verbose_name_plural = 'Местонахождение устройств'