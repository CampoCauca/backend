
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
    
    
    
    #--------------------------------------------URL Movimiento------------------------------------------------------------------------#
    
    #path('movimiento/', ListadoMovimiento.as_view(template_name = "crud/movimiento/tables.html"), name='leermov'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Movimiento o registro 
    #path('movimiento/detalle/<int:pk>', MovimientoDetalle.as_view(template_name = "crud/movimiento/detalle.html"), name='detallesmov'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Movimiento o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    #path('movimiento/editar/<int:pk>', MovimientoActualizar.as_view(template_name = "crud/movimiento/actualizar.html"), name='actualizarmov'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Movimiento o registro de la Base de Datos 
    #path('movimiento/eliminar/<int:pk>', MovimientoEliminar.as_view(), name='crud/movimiento/eliminar.html'), 

    
          #--------------------------------------------URL EMPRESA------------------------------------------------------------------------#
    
    path('empresa/', ListadoEmpresa.as_view(template_name = "crud/empresa/tables.html"), name='leerem'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un EMPRESA o registro 
    path('empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "crud/empresa/detalle.html"), name='detallesem'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo EMPRESA o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un EMPRESAo registro de la Base de Datos 
    path('empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "crud/empresa/actualizar.html"), name='actualizarem'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='crud/empresa/eliminar.html'), 
    
    
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
    
 
  #--------------------------------------------URL Departamento------------------------------------------------------------------------#
    
    path('departamento/', ListadoDepartamento.as_view(template_name = "crud/departamento/tables.html"), name='leerdep'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('departamento/detalle/<int:pk>', DepartamentoDetalle.as_view(template_name = "crud/departamento/detalle.html"), name='detallesdep'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('departamento/editar/<int:pk>', DepartamentoActualizar.as_view(template_name = "crud/departamento/actualizar.html"), name='actualizardep'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('departamento/eliminar/<int:pk>', DepartamentoEliminar.as_view(), name='crud/departamento/eliminar.html'), 
    

#--------------------------------------------URL Municipio------------------------------------------------------------------------#
    
    path('municipio/', ListadoMunicipio.as_view(template_name = "crud/municipio/tables.html"), name='leermu'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('municipio/detalle/<int:pk>', MunicipioDetalle.as_view(template_name = "crud/municipio/detalle.html"), name='detallesmu'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('municipio/editar/<int:pk>', MunicipioActualizar.as_view(template_name = "crud/municipio/actualizar.html"), name='actualizarmu'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('municipio/eliminar/<int:pk>', MunicipioEliminar.as_view(), name='crud/municipio/eliminar.html'),
#--------------------------------------------URL Tipo Identificacion ------------------------------------------------------------------------#
    
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
#--------------------------------------------URL TipoPersona ------------------------------------------------------------------------#
    
    path('tipo_persona/', ListadoTipoPersona.as_view(template_name = "crud/tipo_persona/tables.html"), name='leertpe'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipo_identificacion o registro 
    path('tipo_persona/detalle/<int:pk>', TipoPersonaDetalle.as_view(template_name = "crud/tipo_persona/detalle.html"), name='detallestpe'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('tipo_persona/editar/<int:pk>', TipoPersonaActualizar.as_view(template_name = "crud/tipo_persona/actualizar.html"), name='actualizartpe'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('tipo_persona/eliminar/<int:pk>', TipoPersonaEliminar.as_view(), name='crud/tipo_persona/eliminar.html'), 

#--------------------------------------------URL TipoPersona------------------------------------------------------------------------#
#--------------------------------------------URL TipoDocumento ------------------------------------------------------------------------#
    
    path('tipodocumento/', ListadoTipoDocumento.as_view(template_name = "crud/tipodocumento/tables.html"), name='leertdo'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipo_identificacion o registro 
    path('tipodocumento/detalle/<int:pk>', TipoDocumentoDetalle.as_view(template_name = "crud/tipodocumento/detalle.html"), name='detallestdo'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('tipodocumento/editar/<int:pk>', TipoDocumentoActualizar.as_view(template_name = "crud/tipodocumento/actualizar.html"), name='actualizartdo'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('tipodocumento/eliminar/<int:pk>', TipoDocumentoEliminar.as_view(), name='crud/tipodocumento/eliminar.html'), 

#--------------------------------------------URL TipoDocumento------------------------------------------------------------------------#
#--------------------------------------------URL Persona ------------------------------------------------------------------------#
    
    path('persona/', ListadoPersona.as_view(template_name = "crud/persona/tables.html"), name='leerper'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipo_identificacion o registro 
    path('persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "crud/persona/detalle.html"), name='detallesper'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "crud/persona/actualizar.html"), name='actualizarper'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('persona/eliminar/<int:pk>', PersonaEliminar.as_view(), name='crud/persona/eliminar.html'),
#--------------------------------------------URL Persona ------------------------------------------------------------------------#
#--------------------------------------------DjangoMigrations------------------------------------------------------------------------#
    
    path('django_migrations/', ListadoDjangoMigrations.as_view(template_name = "crud/django_migrations/tables.html"), name='leerdjm'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('django_migrations/detalle/<int:pk>', DjangoMigrationsDetalle.as_view(template_name = "crud/django_migrations/detalle.html"), name='detallesdjm'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('django_migrations/editar/<int:pk>', DjangoMigrationsActualizar.as_view(template_name = "crud/django_migrations/actualizar.html"), name='actualizardjm'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('django_migrations/eliminar/<int:pk>', DjangoMigrationsEliminar.as_view(), name='crud/django_migrations/eliminar.html'), 
   #--------------------------------------------DjangoMigrations------------------------------------------------------------------------#
#--------------------------------------------URL auth_user_user_permissions ------------------------------------------------------------------------#
    
    path('auth_user_user_permissions/', ListadoAuthUserUserPermissions.as_view(template_name = "crud/auth_user_user_permissions/tables.html"), name='leerau'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('auth_user_user_permissions/detalle/<int:pk>', AuthUserUserPermissionsDetalle.as_view(template_name = "crud/auth_user_user_permissions/detalle.html"), name='detallesau'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('auth_user_user_permissions/editar/<int:pk>', AuthUserUserPermissionsActualizar.as_view(template_name = "crud/auth_user_user_permissions/actualizar.html"), name='actualizarau'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('auth_user_user_permissions/eliminar/<int:pk>', AuthUserUserPermissionsEliminar.as_view(), name='crud/auth_user_user_permissions/eliminar.html'), 

    #--------------------------------------------URL auth_user_user_permission ------------------------------------------------------------------------#
#----------------------------------------url cabeza-----------------------------------------------------#
    # Ruta para listar 
    path('cabeza/', ListadoCabeza.as_view(template_name="crud/Cabeza/tables.html"), name='leercab'),

    # Ruta para ver los detalles
    path('cabeza/detalle/<int:pk>', CabezaDetalle.as_view(template_name="crud/Cabeza/detalle.html"), name='detallescab'),

    # Ruta para crear 
    path('cabeza/crear', CabezaCrear.as_view(template_name="crud/Cabeza/crear.html"), name='crearcab'),

    # Ruta para actualizar 
    path('cabeza/editar/<int:pk>', CabezaActualizar.as_view(template_name="crud/Cabeza/actualizar.html"), name='actualizarcab'),

    # Ruta para eliminar 
    path('cabeza/eliminar/<int:pk>', CabezaEliminar.as_view(), name='eliminarcab'),

    path('metodo_pago/eliminar/<int:pk>', MetodoPagoEliminar.as_view(), name='crud/metodo_pago/eliminar.html'),
#----------------------------------------url cabeza-----------------------------------------------------#
#--------------------------------------------URL Articulo------------------------------------------------------------------------#
    
    path('articulo/', ListadoArticulo.as_view(template_name = "crud/articulo/tables.html"), name='leerart'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('articulo/detalle/<int:pk>', ArticuloDetalle.as_view(template_name = "crud/articulo/detalle.html"), name='detallesart'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('articulo/editar/<int:pk>', ArticuloActualizar.as_view(template_name = "crud/articulo/actualizar.html"), name='actualizarart'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('articulo/eliminar/<int:pk>', ArticuloEliminar.as_view(), name='crud/articulo/eliminar.html'),
    #--------------------------------------------URL Articulo------------------------------------------------------------------------#
    #--------------------------------------------URL AuthGroupPermissions------------------------------------------------------------------------#
    
    path('auth_group_permission/', ListadoAuthGroupPermissions.as_view(template_name = "crud/auth_group_permission/tables.html"), name='leerauthgp'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('auth_group_permission/detalle/<int:pk>', AuthGroupPermissionsDetalle.as_view(template_name = "crud/auth_group_permission/detalle.html"), name='detallesauthgp'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('auth_group_permission/editar/<int:pk>', AuthGroupPermissionsActualizar.as_view(template_name = "crud/auth_group_permission/actualizar.html"), name='actualizarauthgp'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('auth_group_permission/eliminar/<int:pk>', AuthGroupPermissionsEliminar.as_view(), name='crud/auth_group_permission/eliminar.html'),
    #--------------------------------------------URL AuthGroupPermissions------------------------------------------------------------------------#
    
    #--------------------------------------------URL AuthPermission------------------------------------------------------------------------#
    
    path('auth_permission/', ListadoAuthPermission.as_view(template_name = "crud/auth_permission/tables.html"), name='leeraut'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('auth_permission/detalle/<int:pk>', AuthPermissionDetalle.as_view(template_name = "crud/auth_permission/detalle.html"), name='detallesaut'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('auth_permission/editar/<int:pk>', AuthPermissionActualizar.as_view(template_name = "crud/auth_permission/actualizar.html"), name='actualizaraut'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('auth_permission/eliminar/<int:pk>', AuthPermissionEliminar.as_view(), name='crud/auth_permission/eliminar.html'), 

    #--------------------------------------------URL AuthPermission------------------------------------------------------------------------#
    #--------------------------------------------URL Cuerpo------------------------------------------------------------------------#
    
    path('cuerpo/', ListadoCuerpo.as_view(template_name = "crud/cuerpo/tables.html"), name='leercur'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('cuerpo/detalle/<int:pk>', CuerpoDetalle.as_view(template_name = "crud/cuerpo/detalle.html"), name='detallescur'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('cuerpo/editar/<int:pk>', CuerpoActualizar.as_view(template_name = "crud/cuerpo/actualizar.html"), name='actualizarcur'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('cuerpo/eliminar/<int:pk>', CuerpoEliminar.as_view(), name='crud/cuerpo/eliminar.html'), 

    #--------------------------------------------URL Cuerpo------------------------------------------------------------------------#
    #--------------------------------------------URL django_content_type------------------------------------------------------------------------#
    
    path('django_content_type/', ContentTypeListado.as_view(template_name = "crud/django_content_type/tables.html"), name='leerContentType'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro o Content Type
    path('django_content_type/detalle/<int:pk>', ContentTypeDetalle.as_view(template_name = "crud/django_content_type/detalle.html"), name='detallesContentType'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro o Content Type de la Base de Datos 
    path('django_content_type/editar/<int:pk>', ContentTypeActualizar.as_view(template_name = "crud/django_content_type/actualizar.html"), name='actualizarContentType'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un registro o Content Type de la Base de Datos 
    path('django_content_type/eliminar/<int:pk>', ContentTypeEliminar.as_view(), name='crud/django_content_type/eliminar.html'), 
  #--------------------------------------------URL django_content_type------------------------------------------------------------------------#
  #--------------------------------------------URL Unidad_de_Medida------------------------------------------------------------------------#
    
    path('unidad_de_medida/', ListadoUnidadDeMedida.as_view(template_name = "crud/unidad_de_medida/tables.html"), name='leeruni'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('unidad_de_medida/detalle/<int:pk>', UnidadDeMedidaDetalle.as_view(template_name = "crud/unidad_de_medida/detalle.html"), name='detallesuni'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('unidad_de_medida/editar/<int:pk>', UnidadDeMedidaActualizar.as_view(template_name = "crud/unidad_de_medida/actualizar.html"), name='actualizaruni'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('unidad_de_medida/eliminar/<int:pk>', UnidadDeMedidaEliminar.as_view(), name='crud/unidad_de_medida/eliminar.html'), 

    #--------------------------------------------URL Unidad_de_Medida------------------------------------------------------------------------#


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

    #--------------------------------------------URL stock------------------------------------------------------------------------#
    
    path('stock/', ListadoStock.as_view(template_name = "crud/stock/tables.html"), name='leerstock'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un EMPRESA o registro 
    path('stock/detalle/<int:pk>', StockDetalle.as_view(template_name = "crud/stock/detalle.html"), name='detallesstock'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo EMPRESA o registro  
    #path('zona/crear', ZonaCrear.as_view(template_name = "crud/zona/crear.html"), name='crearre'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un EMPRESAo registro de la Base de Datos 
    path('stock/editar/<int:pk>', StockActualizar.as_view(template_name = "crud/stock/actualizar.html"), name='actualizarstock'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('stock/eliminar/<int:pk>', StockEliminar.as_view(), name='crud/stock/eliminar.html'),

]

