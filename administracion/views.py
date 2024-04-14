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
    #-----------------------------------Categoria-----------------------------------------------------#

    #-----------------------------------Cabeza-----------------------------------------------------#
class ListadoCabeza(CreateView,ListView,SuccessMessageMixin):
    model = Cabeza
    form = Cabeza
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Cabeza creada correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'    
    

class CabezaDetalle (DetailView):
    model =Cabeza

class CabezaCrear(SuccessMessageMixin, CreateView):
    model = Cabeza
    fields = "__all__"
    success_message = 'creada correctamente'  

    def get_success_url(self):
        return reverse('administracion:leerca')  

class CabezaActualizar(SuccessMessageMixin,UpdateView):
    model =Cabeza
    form = Cabeza
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Cabeza Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'
    
class CabezaEliminar(SuccessMessageMixin, DeleteView): 
    model = Cabeza
    form = Cabeza
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cabeza Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'    
    
     #-----------------------------------Cabeza-----------------------------------------------------#

     #-----------------------------------Stock-----------------------------------------------------#

class StockCrear(SuccessMessageMixin, CreateView):
    model = Stock
    fields = "__all__"  # Mostrar todos los campos del modelo Stock en el formulario
    success_message = 'Stock creado correctamente'  # Mensaje de éxito después de crear un nuevo Stock

    def get_success_url(self):
        return reverse('administracion:leerca') 
    
class ListadoStock(CreateView,ListView,SuccessMessageMixin):
    model = Stock
    form = Stock
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='stock creada correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'    
    

class StockDetalle (DetailView):
    model =Stock

class StockActualizar(SuccessMessageMixin,UpdateView):
    model =Stock
    form = Stock
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Cabeza Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'
    
class StockEliminar(SuccessMessageMixin, DeleteView): 
    model = Stock
    form = Stock
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cabeza Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer' 
#-----------------------------------Stock-----------------------------------------------------#


    
