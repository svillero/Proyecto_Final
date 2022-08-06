from django.shortcuts import render
from django.http import HttpResponse
from appentrega.models import Requerimiento
from appentrega.forms import FormularioBusqueda,RequerimientoFormulario





def inicio(request):

    return render(request,'appentrega/index.html',{"mensaje": "Testing"})


def requerimientos(request):

    listado_requerimientos = Requerimiento.objects.all()   
    

    if request.GET.get('nombre_requerimiento'):

        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_requerimientos = Requerimiento.objects.filter(nombre__icontains = data['nombre_requerimiento'])

        return render(request, "appentrega/requerimientos.html", {'requerimientos':listado_requerimientos,'formulario':formulario})
       
    else:
        formulario = FormularioBusqueda()
        return render(request, "appentrega/requerimientos.html", {'requerimientos':listado_requerimientos, 'formulario':formulario})
        
 


def proyectos(request):
    return HttpResponse("proyectos")
    

def clientes(request):
    return HttpResponse("clientes")
    

def colaboradores(request):
    return HttpResponse("colaboradores")

def crear_requerimiento(request):

    if request.method == "GET":
        formulario = RequerimientoFormulario()
        return render(request, "appentrega/formulario.html", {"formulario": formulario})

    else:

        formulario = RequerimientoFormulario(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
            print(data)

            numero = data.get("numero")
            estado = data.get("estado")
            nombre = data.get('nombre')

            requerimiento = Requerimiento(numero = numero, estado=estado, nombre=nombre)

            requerimiento.save()

            return render(request, "appentrega/formulario.html")

        else:
            return HttpResponse("Formulario no valido")



    