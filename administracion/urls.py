
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
#--------------------------------------------URL Muniicpio------------------------------------------------------------------------#
    
    path('municipio/', ListadoMunicipio.as_view(template_name = "crud/municipio/tables.html"), name='leermu'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('municipio/detalle/<int:pk>', MunicipioDetalle.as_view(template_name = "crud/municipio/detalle.html"), name='detallesmu'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('municipio/editar/<int:pk>', MunicipioActualizar.as_view(template_name = "crud/municipio/actualizar.html"), name='actualizarmu'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('municipio/eliminar/<int:pk>', MunicipioEliminar.as_view(), name='crud/municipio/eliminar.html'), 

      #--------------------------------------------URL metodo_pago------------------------------------------------------------------------#
    
    path('metodo_pago/', ListadoMetodoPago.as_view(template_name = "crud/metodo_pago/tables.html"), name='leerme'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('metodo_pago/detalle/<int:pk>', MetodoPagoDetalle.as_view(template_name = "crud/metodo_pago/detalle.html"), name='detallesme'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('metodo_pago/editar/<int:pk>', MetodoPagoActualizar.as_view(template_name = "crud/metodo_pago/actualizar.html"), name='actualizarme'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('metodo_pago/eliminar/<int:pk>', MetodoPagoEliminar.as_view(), name='crud/metodo_pago/eliminar.html'), 
]

