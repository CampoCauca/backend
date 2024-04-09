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

 
#-----------------------------------Movimiento-----------------------------------------------------#
    
class ListadoMovimiento(CreateView,ListView,SuccessMessageMixin):
    model = Movimiento
    form = Movimiento
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Movimiento creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leermov') # Redireccionamos a la vista principal 'leer'    
    

class MovimientoDetalle (DetailView):
    model =Movimiento

class MovimientoActualizar(SuccessMessageMixin,UpdateView):
    model =Movimiento
    form = Movimiento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Movimiento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leermov') # Redireccionamos a la vista principal 'leer'
    
class MovimientoEliminar(SuccessMessageMixin, DeleteView): 
    model = Movimiento
    form = Movimiento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Movimiento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leermov') # Redireccionamos a la vista principal 'leer'     
     
 #-----------------------------------Movimiento-----------------------------------------------------#

