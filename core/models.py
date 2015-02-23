# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Cotizador(models.Model):
    """
    Información de los clientes que desean tener un contacto con Soluciones Simples
    """
    
    categoria = models.ManyToManyField('core.Categoria', verbose_name=u'Categoría', help_text=u'Elegir todas las que apliquen')
    ciudad = models.ForeignKey('core.Ciudad', verbose_name=u'Ciudad')
    barrio = models.ForeignKey('core.Barrio', verbose_name=u'Barrio')
    nombres = models.CharField(max_length=255, verbose_name=u'Nombres')
    apellidos = models.CharField(max_length=255, verbose_name=u'Apellidos')
    celular = models.CharField(max_length=15, verbose_name=u'Celular')
    direccion = models.CharField(max_length=255, verbose_name=u'Dirección')
    mensaje = models.TextField(verbose_name=u'Mensaje')
    email = models.EmailField(max_length=100, verbose_name=u'Email')
    fecha_creacion = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Cotizador"
        get_latest_by = "fecha_creacion"
        ordering = ['fecha_creacion']

class Categoria(models.Model):
    
    categoria = models.CharField(max_length=255, verbose_name=u'Categoría')
	
    def __unicode__(self):
        return self.categoria
    
    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['categoria']


class Barrio(models.Model):

    #ciudad = models.ForeignKey(Ciudad)
    barrio = models.CharField(max_length=255, verbose_name=u'Barrio')

    def __unicode__(self):
        return self.barrio

    class Meta:
        verbose_name_plural = "Barrios"
        ordering = ['barrio']


class Ciudad(models.Model):
    
    ciudad = models.CharField(max_length=255, verbose_name=u'Ciudad')
	
    def __unicode__(self):
        return self.ciudad

    class Meta:
        verbose_name_plural = "Ciudades"
        ordering = ['ciudad']

class Trabajo(models.Model):
    """
    Información de los clientes que desean tener un contacto con Soluciones Simples
    """
    user = models.ForeignKey(User)
    id_servicio = models.CharField(unique=True, max_length=10,verbose_name=u'Número del Servicio')
    nombre_servicio = models.CharField(max_length=75,verbose_name=u'Nombre del Servicio')
    diagnostico_previo = models.TextField(verbose_name=u'Diagnostico Previo')
    solucion = models.TextField(verbose_name=u'Solución')
    cotizacion = models.IntegerField(verbose_name=u'Valor de la Cotización')
    fecha_creacion = models.DateField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(Trabajo, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return str(self.id_servicio) + " - " + str(self.nombre_servicio)

    class Meta:
        verbose_name_plural = "Trabajos"
        ordering = ['id_servicio']


class ReporteDiario(models.Model):
    """
    Información de los clientes que desean tener un contacto con Soluciones Simples
    """
    user = models.ForeignKey(User)
    trabajo = models.ForeignKey('core.Trabajo',verbose_name=u'Trabajo a Reportar')
    report = models.TextField(verbose_name=u'Reporte')
    foto1 = models.ImageField(verbose_name =u'Foto1', upload_to='Reporte')
    foto2 = models.ImageField(verbose_name =u'Foto2',upload_to='Reporte',null = True, blank = True)
    foto3 = models.ImageField(verbose_name =u'Foto3',upload_to='Reporte',null = True, blank = True)
    foto4 = models.ImageField(verbose_name =u'Foto4',upload_to='Reporte',null = True, blank = True)
    fecha_creacion = models.DateField(auto_now=True)

    def __unicode__(self):
        return str(self.trabajo)

    class Meta:
        verbose_name_plural = "Reportes Diarios"
        ordering = ['fecha_creacion']


class ItemCotizacion(models.Model):
    """
    Información de los clientes que desean tener un contacto con Soluciones Simples
    """
    trabajo = models.ForeignKey('core.Trabajo',verbose_name=u'Trabajo')
    item = models.CharField(max_length=100, verbose_name=u'Item')
    valor = models.IntegerField(verbose_name=u'Valor')

    def __init__(self, *args, **kwargs):
        super(ItemCotizacion, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.item

    class Meta:
        verbose_name_plural = "Cotizacion Item"
        get_latest_by = "fecha_creacion"
