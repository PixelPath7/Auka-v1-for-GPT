from django.shortcuts import render
from .models import Producto, Servicio, Evento, ArticuloBlog, Categoria

def home(request):
    productos = Producto.objects.filter(activo=True)
    servicios = Servicio.objects.all()
    eventos = Evento.objects.filter(activo=True)[:3]
    articulos = ArticuloBlog.objects.filter(activo=True)[:3]
    
    context = {
        'productos': productos,
        'servicios': servicios,
        'eventos': eventos,
        'articulos': articulos,
    }
    return render(request, 'core/index.html', context)

def productos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(activo=True)
    
    categoria_seleccionada = request.GET.get('categoria')
    if categoria_seleccionada:
        productos = productos.filter(categoria_id=categoria_seleccionada)
    
    context = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'core/productos.html', context)

def servicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'core/servicios.html', context)

def about(request):
    return render(request, 'core/about.html')

def blog(request):
    articulos = ArticuloBlog.objects.filter(activo=True)
    context = {'articulos': articulos}
    return render(request, 'core/blog.html', context)

def contacto(request):
    return render(request, 'core/contacto.html')