from django.shortcuts import render
from django.http import HttpResponse
from appentrega.models import Familiar


def inicio(request):
    return HttpResponse("Vista de inicio")


def estudiante(request):
    return HttpResponse("Vista de estudiante")


def profesor(request):
    return HttpResponse("Vista de profesor")

def entregable(request):
    return HttpResponse("Vista de entregable")



def familiares(request):

    familiares = Familiar.objects.all()
    
    lista_familiares = []

    for familiar in familiares:
        lista_familiares.append(familiar.nombre)

    return HttpResponse(lista_familiares)