from django.contrib import admin
from .models import Categoria, Producto, Servicio, Evento, ArticuloBlog

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio_referencia', 'activo']
    list_filter = ['categoria', 'activo']
    search_fields = ['nombre', 'descripcion']

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion']
    search_fields = ['nombre', 'descripcion']

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'ubicacion', 'activo']
    list_filter = ['activo', 'fecha']
    search_fields = ['titulo', 'descripcion']

@admin.register(ArticuloBlog)
class ArticuloBlogAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_publicacion', 'activo']
    list_filter = ['activo', 'fecha_publicacion']
    search_fields = ['titulo', 'contenido']