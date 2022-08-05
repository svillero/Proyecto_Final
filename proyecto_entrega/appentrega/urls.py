from django.urls import path
from appentrega.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("requerimientos/",requerimientos, name='requerimientos'),
    path("proyectos/",proyectos, name='proyectos'),
    path("clientes/",clientes, name='clientes'),
    path("colaboradores/",colaboradores, name='colaboradores')
]