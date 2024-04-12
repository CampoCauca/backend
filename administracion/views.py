from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.contrib import messages 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin 

# Create your views here.

def Home(request):
    
    return render (request, "index.html")

#-----------------------------------Categoria-----------------------------------------------------#
    
class ListadoMunicipio(CreateView,ListView,SuccessMessageMixin):
    model = Municipio
    form = Municipio
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Municipio creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leermu') # Redireccionamos a la vista principal 'leer'    
    

class MunicipioDetalle (DetailView):
    model =Municipio

class MunicipioActualizar(SuccessMessageMixin,UpdateView):
    model =Municipio
    form = Municipio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Municipio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leermu') # Redireccionamos a la vista principal 'leer'
    
class MunicipioEliminar(SuccessMessageMixin, DeleteView): 
    model = Municipio
    form = Municipio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Municipio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leermu') # Redireccionamos a la vista principal 'leer'     
     
 #-----------------------------------Municipio-----------------------------------------------------#
#-----------------------------------Categoria-----------------------------------------------------#
    
class ListadoCategoria(CreateView,ListView,SuccessMessageMixin):
    model = Categoria
    form = Categoria
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Categoria creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'    
    

class CategoriaDetalle (DetailView):
    model =Categoria

class CategoriaActualizar(SuccessMessageMixin,UpdateView):
    model =Categoria
    form = Categoria
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'
    
class CategoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoria
    form = Categoria
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'     
     
 #-----------------------------------Categoria-----------------------------------------------------#

 #-----------------------------------Metodo_pago-----------------------------------------------------#
    
class ListadoMetodoPago(CreateView,ListView,SuccessMessageMixin):
    model = MetodoPago
    form = MetodoPago
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Metodo de pago creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerme') # Redireccionamos a la vista principal 'leer'    
    

class MetodoPagoDetalle (DetailView):
    model =MetodoPago

class MetodoPagoActualizar(SuccessMessageMixin,UpdateView):
    model =MetodoPago
    form = MetodoPago
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Metodo de pago Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerme') # Redireccionamos a la vista principal 'leer'
    
class MetodoPagoEliminar(SuccessMessageMixin, DeleteView): 
    model = MetodoPago
    form = MetodoPago
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Metodo de pago Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerme') # Redireccionamos a la vista principal 'leer'
 #-----------------------------------Metodo_pago-----------------------------------------------------#

 #-----------------------------------DjangoMigrations-----------------------------------------------------#
    
class ListadoDjangoMigrations(CreateView,ListView,SuccessMessageMixin):
    model = DjangoMigrations
    form = DjangoMigrations
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Metodo de pago creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerdjm') # Redireccionamos a la vista principal 'leer'    
    

class DjangoMigrationsDetalle (DetailView):
    model =DjangoMigrations

class DjangoMigrationsActualizar(SuccessMessageMixin,UpdateView):
    model =DjangoMigrations
    form = DjangoMigrations
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Metodo de pago Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerdjm') # Redireccionamos a la vista principal 'leer'
    
class DjangoMigrationsEliminar(SuccessMessageMixin, DeleteView): 
    model = DjangoMigrations
    form = DjangoMigrations
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Metodo de pago Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerdjm') # Redireccionamos a la vista principal 'leer'
#-----------------------------------DjangoMigrations-----------------------------------------------------#
    
