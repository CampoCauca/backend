from django.contrib import admin

from administracion.models import Cabeza, Stock

# Register your models here.
admin.site.register(Stock)
admin.site.register(Cabeza)