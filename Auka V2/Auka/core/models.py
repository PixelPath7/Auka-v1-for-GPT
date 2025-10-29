from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio_referencia = models.DecimalField(max_digits=10, decimal_places=2)
    fotografia = models.ImageField(upload_to='productos/')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.CharField(max_length=50)
    beneficios = models.TextField()
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='eventos/', blank=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
    
    def __str__(self):
        return self.titulo

class ArticuloBlog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/', blank=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Artículo del Blog"
        verbose_name_plural = "Artículos del Blog"
    
    def __str__(self):
        return self.titulo