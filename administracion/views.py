from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


def Home(request):

    return render(request, "index.html")



# -----------------------------------Categoria-----------------------------------------------------#


class ListadoCategoria(CreateView, ListView, SuccessMessageMixin):
    model = Categoria
    form = Categoria
    fields = "__all__"
    context_object_name = "object_list"
    success_message = "Categoria creado correctamente"

    def get_success_url(self):
        return reverse(
            "administracion:leerca"
        )  # Redireccionamos a la vista principal 'leer'


class CategoriaDetalle(DetailView):
    model = Categoria


class CategoriaActualizar(SuccessMessageMixin, UpdateView):
    model = Categoria
    form = Categoria
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos
    success_message = "Categoria Actualizado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre

    def get_success_url(self):
        return reverse(
            "administracion:leerca"
        )  # Redireccionamos a la vista principal 'leer'


class CategoriaEliminar(SuccessMessageMixin, DeleteView):
    model = Categoria
    form = Categoria
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = "Categoria Eliminado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse(
            "administracion:leerca"
        )  # Redireccionamos a la vista principal 'leer'


# -----------------------------------Categoria-----------------------------------------------------#

# -----------------------------------Movimiento-----------------------------------------------------#


class ListadoMovimiento(CreateView, ListView, SuccessMessageMixin):
    model = Movimiento
    form = Movimiento
    fields = "__all__"
    context_object_name = "object_list"
    success_message = "Movimiento creado correctamente"

    def get_success_url(self):
        return reverse(
            "administracion:leermov"
        )  # Redireccionamos a la vista principal 'leer'


class MovimientoDetalle(DetailView):
    model = Movimiento


class MovimientoActualizar(SuccessMessageMixin, UpdateView):
    model = Movimiento
    form = Movimiento
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos
    success_message = "Movimiento Actualizado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre

    def get_success_url(self):
        return reverse(
            "administracion:leermov"
        )  # Redireccionamos a la vista principal 'leer'


class MovimientoEliminar(SuccessMessageMixin, DeleteView):
    model = Movimiento
    form = Movimiento

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):

        success_message = "Movimiento Eliminado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse(
            "administracion:leermov"
        )  # Redireccionamos a la vista principal 'leer'


# -----------------------------------Movimiento-----------------------------------------------------#

# -----------------------------------Empresa-----------------------------------------------------#


class ListadoEmpresa(CreateView, ListView, SuccessMessageMixin):
    model = Empresa
    form = Empresa
    fields = "__all__"
    context_object_name = "object_list"
    success_message = "Empresa creado correctamente"

    def get_success_url(self):
        return reverse(
            "administracion:leerem"
        )  # Redireccionamos a la vista principal 'leer'


class EmpresaDetalle(DetailView):
    model = Empresa


class EmpresaActualizar(SuccessMessageMixin, UpdateView):
    model = Empresa
    form = Empresa
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos
    success_message = "Empresa Actualizado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre

    def get_success_url(self):
        return reverse(
            "administracion:leerem"
        )  # Redireccionamos a la vista principal 'leer'


class EmpresaEliminar(SuccessMessageMixin, DeleteView):
    model = Empresa
    form = Empresa

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):

        success_message = "Empresa Eliminado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse(
            "administracion:leerem"
        )  # Redireccionamos a la vista principal 'leer'


# -----------------------------------Empresa-----------------------------------------------------#


# -----------------------------------Metodo_pago-----------------------------------------------------#


class ListadoMetodoPago(CreateView, ListView, SuccessMessageMixin):
    model = MetodoPago
    form = MetodoPago
    fields = "__all__"
    context_object_name = "object_list"
    success_message = "Metodo de pago creado correctamente"

    def get_success_url(self):
        return reverse(
            "administracion:leerme"
        )  # Redireccionamos a la vista principal 'leer'


class MetodoPagoDetalle(DetailView):
    model = MetodoPago


class MetodoPagoActualizar(SuccessMessageMixin, UpdateView):
    model = MetodoPago
    form = MetodoPago
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos
    success_message = "Metodo de pago Actualizado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre

    def get_success_url(self):
        return reverse(
            "administracion:leerme"
        )  # Redireccionamos a la vista principal 'leer'


class MetodoPagoEliminar(SuccessMessageMixin, DeleteView):
    model = MetodoPago
    form = MetodoPago
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = "Metodo de pago Eliminado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse(
            "administracion:leerme"
        )  # Redireccionamos a la vista principal 'leer'


# -----------------------------------Metodo de pago-----------------------------------------------------#


# -----------------------------------Departamento-----------------------------------------------------#


class ListadoDepartamento(CreateView, ListView, SuccessMessageMixin):
    model = Departamento
    form = Departamento
    fields = "__all__"
    context_object_name = "object_list"
    success_message = "Departamento creado correctamente"

    def get_success_url(self):
        return reverse(
            "administracion:leerdep"
        )  # Redireccionamos a la vista principal 'leer'


class DepartamentoDetalle(DetailView):
    model = Departamento


class DepartamentoActualizar(SuccessMessageMixin, UpdateView):
    model = Departamento
    form = Departamento
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos
    success_message = "Departamento Actualizado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre

    def get_success_url(self):
        return reverse(
            "administracion:leerdep"
        )  # Redireccionamos a la vista principal 'leer'


class DepartamentoEliminar(SuccessMessageMixin, DeleteView):
    model = Departamento
    form = Departamento
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = "Departamento Eliminado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse(
            "administracion:leerdep"
        )  # Redireccionamos a la vista principal 'leer'


# -----------------------------------Departamento-----------------------------------------------------#



# -----------------------------------Municipio-----------------------------------------------------#


class ListadoMunicipio(CreateView, ListView, SuccessMessageMixin):
    model = Municipio
    form = Municipio
    fields = "__all__"
    context_object_name = "object_list"
    success_message = "Municipio creado correctamente"

    def get_success_url(self):
        return reverse(
            "administracion:leermu"
        )  # Redireccionamos a la vista principal 'leer'


class MunicipioDetalle(DetailView):
    model = Municipio


class MunicipioActualizar(SuccessMessageMixin, UpdateView):
    model = Municipio
    form = Municipio
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos
    success_message = "Municipio Actualizado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre

    def get_success_url(self):
        return reverse(
            "administracion:leermu"
        )  # Redireccionamos a la vista principal 'leer'


class MunicipioEliminar(SuccessMessageMixin, DeleteView):
    model = Municipio
    form = Municipio
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = "Municipio Eliminado Correctamente !"  # Mostramos este Mensaje luego de Editar un Postre
        messages.success(self.request, (success_message))
        return reverse(
            "administracion:leermu"
        )  # Redireccionamos a la vista principal 'leer'


# -----------------------------------Municipio-----------------------------------------------------#

#------------------------------------Tipo Idenfiticacion ----------------------------------#
class ListadoTipoIdentificacion(CreateView,ListView,SuccessMessageMixin):
    model = TipoIdentificacion
    form = TipoIdentificacion
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='TipoIdentificacion creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leertip') # Redireccionamos a la vista principal 'leer'    
    

class TipoIdentificacionDetalle (DetailView):
    model =TipoIdentificacion

class TipoIdentificacionActualizar(SuccessMessageMixin,UpdateView):
    model =TipoIdentificacion
    form = TipoIdentificacion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'TipoIdentificacion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leertip') # Redireccionamos a la vista principal 'leer'
    
class TipoIdentificacionEliminar(SuccessMessageMixin, DeleteView): 
    model = TipoIdentificacion
    form = TipoIdentificacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'TipoIdentificacion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leertip') # Redireccionamos a la vista principal 'leer'
    #------------------------------------Tipo Idenfiticacion ----------------------------------#
    #------------------------------------Tipo Persona ----------------------------------#
class ListadoTipoPersona(CreateView,ListView,SuccessMessageMixin):
    model = TipoPersona
    form = TipoPersona
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='TipoPersona creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leertpe') # Redireccionamos a la vista principal 'leer'    
    

class TipoPersonaDetalle (DetailView):
    model =TipoPersona

class TipoPersonaActualizar(SuccessMessageMixin,UpdateView):
    model =TipoPersona
    form = TipoPersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'TipoPersona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leertpe') # Redireccionamos a la vista principal 'leer'
    
class TipoPersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = TipoPersona
    form = TipoPersona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'TipoPersona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leertpe') # Redireccionamos a la vista principal 'leer'
    #------------------------------------Tipo Persona ----------------------------------#