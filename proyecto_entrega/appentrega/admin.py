from django.contrib import admin
from appentrega.models import Requerimiento,Proyecto, Cliente, Colaborador, Avatar

# Register your models here.
admin.site.register(Requerimiento)

admin.site.register(Proyecto)

admin.site.register(Cliente)

admin.site.register(Colaborador)

admin.site.register(Avatar)