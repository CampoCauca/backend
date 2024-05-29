from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
# Extensiones  para seguridad
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import MyUserCreationForm, LoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = MyUserCreationForm()
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(request, email=email, password=password,first_name=first_name,last_name=last_name)
            if user is not None:
                login(request, user)
                
                return redirect( 'index' )
            else:
                error = 'Correo electrónico o contraseña incorrectos'
    else:
        form = LoginForm()
        error = 'Correo electrónico o contraseña incorrectos'
    return render(request, 'login.html', {'form': form, 'error': error})
   

   

def Perfil(request):
    return render (request, "perfil/perfil.html")


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
    #------------------------------------TipoDocumento ----------------------------------#
class ListadoTipoDocumento(CreateView,ListView,SuccessMessageMixin):
    model = TipoDocumento
    form = TipoDocumento
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='TipoDocumento creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leertdo') # Redireccionamos a la vista principal 'leer'    
    

class TipoDocumentoDetalle (DetailView):
    model =TipoDocumento

class TipoDocumentoActualizar(SuccessMessageMixin,UpdateView):
    model =TipoDocumento
    form = TipoDocumento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'TipoDocumento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leertdo') # Redireccionamos a la vista principal 'leer'
    
class TipoDocumentoEliminar(SuccessMessageMixin, DeleteView): 
    model = TipoDocumento
    form = TipoDocumento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'TipoDocumento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leertdo') # Redireccionamos a la vista principal 'leer'
    #------------------------------------TipoDocumento ----------------------------------#
#-----------------------------------Persona-----------------------------------------------------#
    
class ListadoPersona(CreateView,ListView,SuccessMessageMixin):
    model = Persona
    form = Persona
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Persona creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerper') # Redireccionamos a la vista principal 'leer'    
    

class PersonaDetalle (DetailView):
    model =Persona

class PersonaActualizar(SuccessMessageMixin,UpdateView):
    model =Persona
    form = Persona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Persona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerper') # Redireccionamos a la vista principal 'leer'
    
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona
    form = Persona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Persona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerper') # Redireccionamos a la vista principal 'leer'
     #-----------------------------------Persona-----------------------------------------------------#
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
 #-----------------------------------AuthUserUserPermissions-----------------------------------------------------#
    
class ListadoAuthUserUserPermissions(CreateView,ListView,SuccessMessageMixin):
    model = AuthUserUserPermissions
    form = AuthUserUserPermissions
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='AuthUserUserPermissions creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerau') # Redireccionamos a la vista principal 'leer'    
    

class AuthUserUserPermissionsDetalle (DetailView):
    model =AuthUserUserPermissions

class AuthUserUserPermissionsActualizar(SuccessMessageMixin,UpdateView):
    model = AuthUserUserPermissions
    form = AuthUserUserPermissions
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'AuthUserUserPermissions Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerau') # Redireccionamos a la vista principal 'leer'
    
class AuthUserUserPermissionsEliminar(SuccessMessageMixin, DeleteView): 
    model = AuthUserUserPermissions
    form = AuthUserUserPermissions
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'AuthUserUserPermissions Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerau') # Redireccionamos a la vista principal 'leer'     
     
 #-----------------------------------AuthUserUserPermissions-----------------------------------------------------#
    #-----------------------------------Cabeza-----------------------------------------------------#
class ListadoCabeza(CreateView,ListView,SuccessMessageMixin):
    model = Cabeza
    form = Cabeza
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Cabeza creada correctamente'
    def get_success_url(self):        
        return reverse('administracion:leercab') # Redireccionamos a la vista principal 'leer'    
    

class CabezaDetalle (DetailView):
    model =Cabeza

class CabezaCrear(SuccessMessageMixin, CreateView):
    model = Cabeza
    fields = "__all__"
    success_message = 'creada correctamente'  

    def get_success_url(self):
        return reverse('administracion:leercab')  

class CabezaActualizar(SuccessMessageMixin,UpdateView):
    model =Cabeza
    form = Cabeza
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Cabeza Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leercab') # Redireccionamos a la vista principal 'leer'
    
class CabezaEliminar(SuccessMessageMixin, DeleteView): 
    model = Cabeza
    form = Cabeza
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cabeza Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leercab') # Redireccionamos a la vista principal 'leer'


#     def get_success_url(self):               
#         return reverse('administracion:leerca') # Redireccionamos a la vista principal 'leer'
    
# from django.urls import reverse
# from django.contrib.messages.views import SuccessMessageMixin
# from django.views.generic.edit import DeleteView
# from .models import Cabeza

# class CabezaEliminar(SuccessMessageMixin, DeleteView):
#     model = Cabeza
#     success_message = "El registro fue eliminado exitosamente"  # Mensaje a mostrar tras eliminar el objeto
    
#     def get_success_url(self):
#         return reverse('administracion:leerme')  # Redireccionamos a la vista principal 'leerme'
    
#----------------------------------------------------Cabeza-----------------------------------------------------#
 #-----------------------------------Articulo-----------------------------------------------------#
 
class ListadoArticulo(CreateView,ListView,SuccessMessageMixin):
    model = Articulo
    form = Articulo
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Articulo creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerart') # Redireccionamos a la vista principal 'leer'    
    

class ArticuloDetalle (DetailView):
    model =Articulo

class ArticuloActualizar(SuccessMessageMixin,UpdateView):
    model =Articulo
    form = Articulo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Articulo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerart') # Redireccionamos a la vista principal 'leer'
    
class ArticuloEliminar(SuccessMessageMixin, DeleteView): 
    model = Articulo
    form = Articulo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Articulo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerart') # Redireccionamos a la vista principal 'leer'     
     
 #-----------------------------------Articulo-----------------------------------------------------#
 #-----------------------------------AuthGroupPermissions-----------------------------------------------------#
 
class ListadoAuthGroupPermissions(CreateView,ListView,SuccessMessageMixin):
    model = AuthGroupPermissions
    form = AuthGroupPermissions
    fields = "_all_"
    context_object_name = 'object_list'
    success_message ='AuthGroupPermissions creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerauthgp') # Redireccionamos a la vista principal 'leer'    
    

class AuthGroupPermissionsDetalle (DetailView):
    model = AuthGroupPermissions

class AuthGroupPermissionsActualizar(SuccessMessageMixin,UpdateView):
    model = AuthGroupPermissions
    form = AuthGroupPermissions
    fields = "_all_" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'AuthGroupPermissions Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leerauthgp') # Redireccionamos a la vista principal 'leer'
    
class AuthGroupPermissionsEliminar(SuccessMessageMixin, DeleteView): 
    model = AuthGroupPermissions
    form = AuthGroupPermissions
    fields = "_all_"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'AuthGroupPermissions Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerauthgp') # Redireccionamos a la vista principal 'leer'     
     
 #-----------------------------------AuthGroupPermissions-----------------------------------------------------#
 #-----------------------------------Auth_permission(Permisos de autenticacion)-----------------------------------------------------#
    
class ListadoAuthPermission(CreateView,ListView,SuccessMessageMixin):
    model = AuthPermission
    form = AuthPermission
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Auth permission creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leeraut') # Redireccionamos a la vista principal 'leer'    
    

class AuthPermissionDetalle (DetailView):
    model =AuthPermission

class AuthPermissionActualizar(SuccessMessageMixin,UpdateView):
    model =AuthPermission
    form = AuthPermission
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Auth Permission Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leeraut') # Redireccionamos a la vista principal 'leer'
    
class AuthPermissionEliminar(SuccessMessageMixin, DeleteView): 
    model = AuthPermission
    form = AuthPermission
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Auth Permission Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leeraut') # Redireccionamos a la vista principal 'leer' 

#-----------------------------------Auth_permission(Permisos de autenticacion)-----------------------------------------------------#
#-----------------------------------Cuerpo-----------------------------------------------------#
    
class ListadoCuerpo(CreateView,ListView,SuccessMessageMixin):
    model = Cuerpo
    form = Cuerpo
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Cuerpo creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leercur') # Redireccionamos a la vista principal 'leer'    
    

class CuerpoDetalle (DetailView):
    model =Cuerpo

class CuerpoActualizar(SuccessMessageMixin,UpdateView):
    model =Cuerpo
    form = Cuerpo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Cuerpo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leercur') # Redireccionamos a la vista principal 'leer'
    
class CuerpoEliminar(SuccessMessageMixin, DeleteView): 
    model = Cuerpo
    form = Cuerpo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cuerpo Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leercur') # Redireccionamos a la vista principal 'leer' 

#-----------------------------------Cuerpo-----------------------------------------------------#
#-----------------------------------django_content_type-----------------------------------------------------#

class ContentTypeListado(CreateView,ListView,SuccessMessageMixin):
    model = DjangoContentType
    form = DjangoContentType
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Categoria creado correctamente'
    def get_success_url(self):        
        return reverse('administracion:leerContentType') # Redireccionamos a la vista principal 'leer'    
    

class ContentTypeDetalle (DetailView):
    model = DjangoContentType

class ContentTypeActualizar(SuccessMessageMixin,UpdateView):
    model = DjangoContentType
    form = DjangoContentType
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Content Type' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Content Type

    def get_success_url(self):               
        return reverse('administracion:leerContentType') # Redireccionamos a la vista principal 'leer'
    
class ContentTypeEliminar(SuccessMessageMixin, DeleteView): 
    model = DjangoContentType
    form = DjangoContentType
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Content Type
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Grupo
        messages.success (self.request, (success_message))       
        return reverse('administracion:leerContentType') # Redireccionamos a la vista principal 'leer'    
        
 #-----------------------------------django_content_type-----------------------------------------------------#
 #-----------------------------------Unidad_de_medida-----------------------------------------------------#
    
class ListadoUnidadDeMedida(CreateView,ListView,SuccessMessageMixin):
    model = UnidadDeMedida
    form = UnidadDeMedida
    fields = "__all__"
    context_object_name = 'object_list'
    success_message ='Unidad de medida creada correctamente'
    def get_success_url(self):        
        return reverse('administracion:leeruni') # Redireccionamos a la vista principal 'leer'    
    

class UnidadDeMedidaDetalle (DetailView):
    model =UnidadDeMedida

class UnidadDeMedidaActualizar(SuccessMessageMixin,UpdateView):
    model =UnidadDeMedida
    form = UnidadDeMedida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Unidad de medida Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('administracion:leeruni') # Redireccionamos a la vista principal 'leer'
    
class UnidadDeMedidaEliminar(SuccessMessageMixin, DeleteView): 
    model = UnidadDeMedida
    form = UnidadDeMedida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Unidad de medida Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('administracion:leeruni') # Redireccionamos a la vista principal 'leer' 

#-----------------------------------Unidad_de_medida-----------------------------------------------------#