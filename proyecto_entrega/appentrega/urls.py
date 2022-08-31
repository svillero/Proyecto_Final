from django.urls import path
from appentrega.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio,name="inicio"),
    path("requerimientos/",requerimientos, name='requerimientos'),
    path("requerimiento/",crear_requerimiento, name='crear_requerimiento'),
    path("requerimiento/borrar/<id_requerimiento>", borrar_requerimiento, name="borrar_requerimiento"),
    path("requerimiento/editar/<id_requerimiento>", editar_requerimiento, name="editar_requerimiento"),
    path("proyecto/",crear_proyecto, name='crear_proyecto'),
    path("proyecto/borrar/<id_proyecto>", borrar_proyecto, name="borrar_proyecto"),
    path("proyecto/editar/<id_proyecto>", editar_proyecto, name="editar_proyecto"),
    path("cliente/",crear_cliente, name='crear_cliente'),
    path("cliente/borrar/<id_cliente>", borrar_cliente, name="borrar_cliente"),
    path("cliente/editar/<id_cliente>", editar_cliente, name="editar_cliente"),
    path("colaborador/",crear_colaborador, name='crear_colaborador'),
    path("colaborador/borrar/<id_colaborador>", borrar_colaborador, name="borrar_colaborador"),
    path("colaborador/editar/<id_colaborador>", editar_colaborador, name="editar_colaborador"),
    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("register/", registrar_usuario, name="registro"),
    path("logout/", LogoutView.as_view(template_name="appentrega/autenticacion/logout.html"), name="logout"),
    path("edit/", editar_usuario, name="editar_usuario"),
    path("avatar/", agregar_avatar, name="agregar_avatar")
]