from django.shortcuts import render
from django.http import HttpResponse
from appentrega.models import Requerimiento





def inicio(request):

    return render(request,'appentrega/index.html',{"mensaje": "Testing"})


def requerimientos(request):
    requerimientos = Requerimiento.objects.all()
    
    context = {
        "mensaje": "Todos nuestros cursos al mejor precio!",
        "mensaje_bienvenida": "Bienvenid@s!",
        "requerimientos": requerimientos
    }

    return render(request, "appentrega/requerimientos.html", context)
    


def proyectos(request):
    return HttpResponse("proyectos")
    

def clientes(request):
    return HttpResponse("clientes")
    

def colaboradores(request):
    return HttpResponse("colaboradores")
    