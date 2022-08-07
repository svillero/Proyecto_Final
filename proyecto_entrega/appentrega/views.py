from django.shortcuts import render
from django.http import HttpResponse
from appentrega.models import Requerimiento,Proyecto,Colaborador,Cliente
from appentrega.forms import FormularioBusqueda,RequerimientoFormulario,ProyectoFormulario,ClienteFormulario,ColaboradorFormulario





def inicio(request):

    return render(request, "appentrega/index.html")


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
        
 


def crear_proyecto(request):

  
    
    if request.method == "GET":
        formulario = ProyectoFormulario()
        return render(request, "appentrega/crear_proyecto.html", {"formulario": formulario})

    else:

        formulario = ProyectoFormulario(request.POST)

        if formulario.is_valid():
        
            data = formulario.cleaned_data
            print(data)

            numero = data.get("numero")
            nombre = data.get("nombre")
            pm_asignado = data.get('pm_asignado')
            fecha_alta = data.get('fecha_alta')
            costo = data.get('costo')

            proyecto = Proyecto(numero = numero, nombre=nombre, pm_asignado=pm_asignado, fecha_alta = fecha_alta, costo = costo)

            proyecto.save()

            return render(request, "appentrega/index.html")

        else:
            return HttpResponse("Formulario no valido") 
    

def crear_cliente(request):

    if request.method == "GET":
        formulario = ClienteFormulario()
        return render(request, "appentrega/crear_cliente.html", {"formulario": formulario})

    else:

        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
        
            data = formulario.cleaned_data
            print(data)

            cliente_id = data.get("cliente_id")
            razon_social = data.get("razon_social")
            email = data.get('email')
            fecha_alta = data.get('fecha_alta')
            

            cliente = Cliente(cliente_id = cliente_id, razon_social=razon_social, email=email, fecha_alta = fecha_alta)

            cliente.save()

            return render(request, "appentrega/index.html")

        else:
            return HttpResponse("Formulario no valido") 
    

def crear_colaborador(request):

    if request.method == "GET":
        formulario = ColaboradorFormulario()
        return render(request, "appentrega/crear_colaborador.html", {"formulario": formulario})

    else:

        formulario = ColaboradorFormulario(request.POST)

        if formulario.is_valid():
        
            data = formulario.cleaned_data
            print(data)

            numero = data.get("numero")
            nombre = data.get("nombre")
            apellido = data.get('apellido')
            cargo = data.get('cargo')
            email = data.get('email')
            fecha_alta = data.get('fecha_alta')
            

            colaborador = Colaborador(numero = numero, nombre=nombre, apellido=apellido, cargo = cargo,email =email,fecha_alta=fecha_alta)

            colaborador.save()

            return render(request, "appentrega/index.html")

        else:
            return HttpResponse("Formulario no valido") 

def crear_requerimiento(request):

    
    if request.method == "GET":
        formulario = RequerimientoFormulario()
       
        return render(request, "appentrega/crear_requerimiento.html", {"formulario": formulario})

    else:

        formulario = RequerimientoFormulario(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
            print(data)

            numero = data.get("numero")
            estado = data.get("estado")
            nombre = data.get('nombre')
            solicitud = data.get('solicitud')
            fecha_alta = data.get('fecha_alta')

            requerimiento = Requerimiento(numero = numero, estado=estado, nombre=nombre, solicitud = solicitud, fecha_alta = fecha_alta)

            requerimiento.save()            
            return render(request, "appentrega/index.html")

        else:            
            return HttpResponse("Formulario no valido")
    



    