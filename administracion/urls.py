"""
URL configuration for campocauca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from .views import *

urlpatterns = [
    
      #--------------------------------------------URL Categoria------------------------------------------------------------------------#
    
    path('categoria/', ListadoCategoria.as_view(template_name = "crud/Categoria/tables.html"), name='leerca'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('categoria/detalle/<int:pk>', CategoriaDetalle.as_view(template_name = "crud/Categoria/detalle.html"), name='detallesca'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('categoria/editar/<int:pk>', CategoriaActualizar.as_view(template_name = "crud/Categoria/actualizar.html"), name='actualizarca'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('categoria/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='crud/Categoria/eliminar.html'),

    
      #--------------------------------------------URL Categoria------------------------------------------------------------------------#
    
    path('empresa/', ListadoEmpresa.as_view(template_name = "crud/empresa/tables.html"), name='leerem'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "crud/empresa/detalle.html"), name='detallesem'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "crud/empresa/actualizar.html"), name='actualizarem'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='crud/empresa/eliminar.html'), 
 

    

       #--------------------------------------------URL Movimiento------------------------------------------------------------------------#
    
    path('movimiento/', ListadoMovimiento.as_view(template_name = "crud/movimiento/tables.html"), name='leermov'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Movimiento o registro 
    path('movimiento/detalle/<int:pk>', MovimientoDetalle.as_view(template_name = "crud/movimiento/detalle.html"), name='detallesmov'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Movimiento o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('movimiento/editar/<int:pk>', MovimientoActualizar.as_view(template_name = "crud/movimiento/actualizar.html"), name='actualizarmov'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Movimiento o registro de la Base de Datos 
    path('movimiento/eliminar/<int:pk>', MovimientoEliminar.as_view(), name='crud/movimiento/eliminar.html'), 

]
