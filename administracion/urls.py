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
    
    path('categoria/', ListadoCategoria.as_view(template_name = "crud/categoria/tables.html"), name='leerca'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('categoria/detalle/<int:pk>', CategoriaDetalle.as_view(template_name = "crud/categoria/detalle.html"), name='detallesca'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('categoria/editar/<int:pk>', CategoriaActualizar.as_view(template_name = "crud/categoria/actualizar.html"), name='actualizarca'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('categoria/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='crud/categoria/eliminar.html'), 



    
      #--------------------------------------------URL TipoIdentificacion ------------------------------------------------------------------------#
    
    path('tipoidentificacion/', ListadoTipoIdentificacion.as_view(template_name = "crud/tipo_identificacion/tables.html"), name='leertip'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipo_identificacion o registro 
    path('tipoidentificacion/detalle/<int:pk>', TipoIdentificacionDetalle.as_view(template_name = "crud/tipo_identificacion/detalle.html"), name='detallestip'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('tipoidentificacion/editar/<int:pk>', TipoIdentificacionActualizar.as_view(template_name = "crud/tipo_identificacion/actualizar.html"), name='actualizartip'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('tipoidentificacion/eliminar/<int:pk>', TipoIdentificacionEliminar.as_view(), name='crud/tipo_identificacion/eliminar.html'), 

#--------------------------------------------URL TipoIdentificacion------------------------------------------------------------------------#

]
