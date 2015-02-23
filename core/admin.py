# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class CotizadorAdmin(admin.ModelAdmin):
    """
    Cotizador admin class
    """
    search_fields = ('nombres', 'apellidos')
    list_filter = ('fecha_creacion',) 
    list_display = ('id', 'nombres','apellidos','celular','direccion','fecha_creacion')
    pass

admin.site.register(Cotizador, CotizadorAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    """
    Categoria admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Categoria, CategoriaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    """
    Barrio admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Barrio, BarrioAdmin)

class CiudadAdmin(admin.ModelAdmin):
    """
    Ciudad admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Ciudad, CiudadAdmin)

class TrabajoAdmin(admin.ModelAdmin):
    """
    Ciudad admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date')
    # list_display = ('id', 'name')
    pass

admin.site.register(Trabajo, TrabajoAdmin)

class ReporteDiarioAdmin(admin.ModelAdmin):
    """
    Ciudad admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date')
    # list_display = ('id', 'name')
    pass

admin.site.register(ReporteDiario, ReporteDiarioAdmin)

class ItemCotizacionAdmin(admin.ModelAdmin):
    """
    Ciudad admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date')
    # list_display = ('id', 'name')
    pass

admin.site.register(ItemCotizacion, ItemCotizacionAdmin)