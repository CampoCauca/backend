
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#importación de librerias especificas para modificar el registro de usuarios 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(max_length=45)
    descripcion_articulo = models.CharField(max_length=345)
    # imagen = models.TextField()
    # categoria_id_categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='categoria_id_categoria')
    # unidad_de_medida_idunidad_de_medida = models.ForeignKey('UnidadDeMedida', models.DO_NOTHING, db_column='unidad_de_medida_idunidad_de_medida')
    # persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_id_persona')

    class Meta:
        managed = False
        db_table = 'articulo'
        db_table_comment = 'Esta entidad se crea con el objetivo de mantener un registro de todos los articulos que hay en la tienda, teniendo en cuenta sus caracteristicas '


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
  
        
class MyUser(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True    
    class Meta:
        managed = True
        db_table = 'myuser'
        
class Persona(models.Model):

    id_persona = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre= models.CharField(max_length=45)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=45)
    identificacion = models.CharField(max_length=45)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=45)
    correo_institucional = models.CharField(max_length=70)
    direccion = models.CharField(max_length=45)
    foto = models.ImageField(upload_to = "img/", null=True)
   
    
    class Meta:
        managed = True
        db_table = 'persona'
      
@receiver(post_save, sender=Persona)       
def create_user_for_persona(sender, instance, created, **kwargs):
    if created:
        User = get_user_model()
        email = instance.correop
        first_name = instance.primer_nombre
        last_name = instance.primer_apellido
        password = instance.identificacion  # Aquí puedes definir cómo deseas obtener el valor de la contraseña
        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)        

def actualizar_usuario(sender, instance, **kwargs):
    usuario = instance.user
    usuario.email = instance.email
    usuario.first_name = instance.first_name
    usuario.last_name = instance.last_name
    usuario.save()



class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(MyUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(MyUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cabeza(models.Model):
    id_cabeza = models.AutoField(primary_key=True)
    id_persona = models.CharField(max_length=45)
    fecha = models.DateField()
    valor_total = models.CharField(max_length=45)
    vendedor = models.ForeignKey('Persona', models.DO_NOTHING, db_column='vendedor')
    comprador = models.ForeignKey('Persona', models.DO_NOTHING, db_column='comprador', related_name='cabeza_comprador_set')
    tipo_documento_idtipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='tipo_documento_idtipo_documento')

    class Meta:
        managed = False
        db_table = 'cabeza'
        db_table_comment = 'Esta entidad se crea con el objetivo de visualizar la informacion basica de la tienda, el vendedor, y el comprador'


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=45)
    descipcion_categoria = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'
        db_table_comment = 'Esta entidad se crea con el objetivo de clasificar cada articulo en categorias y a su vez  generar un filtro de busqueda que ayude al usuario o vendedor a encontrar el articulo facilmente '


class Cuerpo(models.Model):
    id_cuerpo = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    valor_total_cuerpo = models.DecimalField(max_digits=10, decimal_places=0)
    articulo_id_articulo = models.ForeignKey(Articulo, models.DO_NOTHING, db_column='articulo_id_articulo')
    cabeza_id_cabeza = models.ForeignKey(Cabeza, models.DO_NOTHING, db_column='cabeza_id_cabeza')

    class Meta:
        managed = False
        db_table = 'cuerpo'
        db_table_comment = 'Esta entidad se crea con el objetivo de poder registrar los articulos seleccionados por el cliente los cuales seran proximos a ser comprados o ya fueron comprados.'


class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=45)
    descripcion_departamento = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'
        db_table_comment = 'Esta entidad se crea con el objetivo de determinar la procedencia por departamentos, o en su defecto dictaminar hacia que punto van dirijido los pedidos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(MyUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=45)
    nit = models.CharField(db_column='Nit', max_length=45)  # Field name made lowercase.
    direccion = models.CharField(max_length=45)
    telefonoemp = models.IntegerField()
    correo = models.CharField(max_length=45)
    empresacol = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'empresa'
        db_table_comment = 'Esta entidad se crea con el objetivo de poder mantener un registro de todos los clientes,en el dicho caso de que este identifique como empresa '


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo = models.CharField(max_length=45)
    descripcion_metodo = models.TextField(blank=True, null=True)
    cabeza_id_cabeza = models.ForeignKey(Cabeza, models.DO_NOTHING, db_column='cabeza_id_cabeza')

    class Meta:
        managed = False
        db_table = 'metodo_pago'
        db_table_comment = 'Esta entidad se crea con el objetivo de llevar acabo una eleccion de los diferentes metodos de pago disponibles segun la facilidad del cliente '


class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    tipo_movimiento = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'movimiento'
        db_table_comment = 'Esta entidad se crea con el objetivo de ver los movimientos de salida y entrada de articulos al stock '


class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=45)
    codigo_municipio = models.CharField(max_length=45)
    departamento_id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_departamento')

    class Meta:
        managed = False
        db_table = 'municipio'
        db_table_comment = 'Esta entidad se crea con el objetivo de determinar la procedencia por municipios, o en su defecto dictaminar hacia que punto van dirijido los pedidos'




class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    cantidad_actual = models.IntegerField()
    valor_compra = models.DecimalField(max_digits=10, decimal_places=0)
    valor_venta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    utilidad = models.CharField(max_length=45)
    movimiento_id_movimiento = models.ForeignKey(Movimiento, models.DO_NOTHING, db_column='movimiento_id_movimiento')
    articulo_id_articulo = models.ForeignKey(Articulo, models.DO_NOTHING, db_column='articulo_id_articulo')

    class Meta:
        managed = False
        db_table = 'stock'
        db_table_comment = 'Esta entidad se crea con el objetivo de llevar un inventario de los articulos que se encunetran disponibles y su valor unitario de compra y venta '


class TipoDocumento(models.Model):
    idtipo_documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_documento'
        db_table_comment = 'Esta entidad se crea con el objetivo de diferenciar los tipos de factura que se puedan tener, como: factura de venta, factura de compra, orden de pedido.'


class TipoIdentificacion(models.Model):
    id_tipo_identificacion = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_identificacion'
        db_table_comment = 'tabla diseñada con el fin de identificar si la persona que se registra  es extrajera, nacional,'


class TipoPersona(models.Model):
    id_tipo_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_persona'
        db_table_comment = 'tabla diseñada con el fin de identificar si la persona que se registra juridica o natural.'


class UnidadDeMedida(models.Model):
    idunidad_de_medida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=145)

    class Meta:
        managed = False
        db_table = 'unidad_de_medida'

