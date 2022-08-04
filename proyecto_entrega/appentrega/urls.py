from django.urls import path
from appentrega.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    # path("cursos/", cursos),
    # path("estudiantes/", estudiante),
    # path("profesores/", profesor),
    # path("entregables/", entregable),
]