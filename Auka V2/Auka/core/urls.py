from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('servicios/', views.servicios, name='servicios'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),
]