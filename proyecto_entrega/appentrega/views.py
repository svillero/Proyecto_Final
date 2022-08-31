
from asyncio.windows_events import NULL
from operator import is_not
from django.shortcuts import render, redirect
from django.http import HttpResponse
from appentrega.models import Requerimiento,Proyecto,Colaborador,Cliente, Avatar
from appentrega.forms import FormularioBusqueda,RequerimientoFormulario,ProyectoFormulario,ClienteFormulario,ColaboradorFormulario

# Auth imports
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from appentrega.forms import UserCustomCreationForm,UserEditForm, AvatarForm


# Permisos de Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def inicio(request):

    if not request.user.is_anonymous:
        try:
            avatares = Avatar.objects.filter(usuario = request.user.id)
            
            return render(request, "appentrega/index.html",{"url": avatares[0].imagen.url})
        except:
            return render(request, "appentrega/index.html")
    else:
        return render(request, "appentrega/index.html")

@login_required
def requerimientos(request):

    listado_requerimientos = Requerimiento.objects.all()   
    

    if request.GET.get('nombre_requerimiento'):

        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_requerimientos = Requerimiento.objects.filter(nombre__icontains = data['nombre_requerimiento'])

        return render(request, "appentrega/componentes/requerimientos.html", {'requerimientos':listado_requerimientos,'formulario':formulario})
       
    else:
        formulario = FormularioBusqueda()
        return render(request, "appentrega/componentes/requerimientos.html", {'requerimientos':listado_requerimientos, 'formulario':formulario})
        
 

@login_required
def crear_cliente(request):  


    clientes = Cliente.objects.all()

    if request.method == "GET":
        formulario = ClienteFormulario()
        context = {
            
            "clientes": clientes,
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/crear_cliente.html", context)

    else:

        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
        
            data = formulario.cleaned_data
            print(data)

            rut = data.get('rut')
            razon_social = data.get("razon_social")
            email = data.get('email')
            fecha_alta = data.get('fecha_alta')
            

            cliente = Cliente(rut = rut, razon_social=razon_social, email=email, fecha_alta = fecha_alta)

            cliente.save()

        formulario = ClienteFormulario()
        context = {
           
            "clientes": clientes,
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/crear_cliente.html", context)

@login_required
def borrar_cliente(request, id_cliente):
    try:
        cliente = Cliente.objects.get(id=id_cliente)        
        cliente.delete()        

        return redirect('crear_cliente')
       
    except:
        return redirect('inicio')

@login_required
def editar_cliente(request, id_cliente):

    if request.method == "GET":
        formulario = ClienteFormulario()
        contexto = {
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/editar_cliente.html", contexto)

    else:

        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data 
            print(data)

            try:
                cliente = Cliente.objects.get(id=id_cliente)
                cliente.rut = data.get("rut")
                cliente.razon_social = data.get('razon_social')
                cliente.email = data.get('email')                
                cliente.fecha_alta = data.get('fecha_alta')            
                
                cliente.save()
            except:
                return HttpResponse("Error en la actualizacion")

        return redirect('crear_cliente')         
    
@login_required
def crear_colaborador(request):

    colaboradores = Colaborador.objects.all()

    if request.method == "GET":
        formulario = ColaboradorFormulario()
        context = {
            
            "colaboradores": colaboradores,
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/crear_colaborador.html", context)

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

        formulario = ColaboradorFormulario()
        context = {
            
            "colaboradores": colaboradores,
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/crear_colaborador.html", context)

@login_required
def borrar_colaborador(request, id_colaborador):
    try:
        colaborador = Colaborador.objects.get(id=id_colaborador)        
        colaborador.delete()        

        return redirect('crear_colaborador')
       
    except:
        return redirect('inicio')

@login_required
def editar_colaborador(request, id_colaborador):

    if request.method == "GET":
        formulario = ColaboradorFormulario()
        contexto = {
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/editar_colaborador.html", contexto)

    else:

        formulario = ColaboradorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data 
            print(data)

            try:
                colaborador = Colaborador.objects.get(id=id_colaborador)
                colaborador.numero = data.get("numero")
                colaborador.nombre = data.get("nombre")
                colaborador.apellido = data.get('apellido')
                colaborador.cargo = data.get('cargo')
                colaborador.email = data.get('email')
                colaborador.fecha_alta = data.get('fecha_alta')       
                
                colaborador.save()
            except:
                return HttpResponse("Error en la actualizacion")

        return redirect('crear_colaborador')         
    
@login_required
def crear_requerimiento(request):

    
    requerimientos = Requerimiento.objects.all()

    if request.method == "GET":
        formulario = RequerimientoFormulario()
        context = {
            
            "requerimientos": requerimientos,
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/crear_requerimiento.html", context)

    else:

        formulario = RequerimientoFormulario(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data          

            numero = data.get("numero")
            estado = data.get("estado")
            nombre = data.get('nombre')
            solicitud = data.get('solicitud')
            fecha_alta = data.get('fecha_alta')
            

            requerimiento = Requerimiento(numero = numero, estado=estado, nombre=nombre, solicitud = solicitud, fecha_alta = fecha_alta)

            requerimiento.save()            
        formulario = RequerimientoFormulario()
        context = {
           
            "requerimientos": requerimientos,
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/crear_requerimiento.html", context)

@login_required
def borrar_requerimiento(request, id_requerimiento):
    try:
        requerimiento = Requerimiento.objects.get(id=id_requerimiento)        
        requerimiento.delete()        

        return redirect('crear_requerimiento')
       
    except:
        return redirect('inicio')

@login_required
def editar_requerimiento(request, id_requerimiento):

    if request.method == "GET":
        formulario = RequerimientoFormulario()
        contexto = {
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/editar_requerimiento.html", contexto)

    else:

        formulario = RequerimientoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data 
            print(data)

            try:
                requerimiento = Requerimiento.objects.get(id=id_requerimiento)
                requerimiento.numero = data.get("numero")
                requerimiento.estado = data.get("estado")
                requerimiento.nombre = data.get('nombre')
                requerimiento.solicitud = data.get('solicitud')
                requerimiento.fecha_alta = data.get('fecha_alta')
                requerimiento.fecha_entrega = data.get('fecha_entrega')      
                
                requerimiento.save()
            except:
                return HttpResponse("Error en la actualizacion")

        return redirect('crear_requerimiento')        

@login_required    
def crear_proyecto(request):


    proyectos = Proyecto.objects.all()

    if request.method == "GET":
        formulario = ProyectoFormulario()

        context = {
            
            "proyectos": proyectos,
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/crear_proyecto.html", context)

    else:
        formulario = ProyectoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            numero = data.get("numero")
            nombre = data.get("nombre")
            pm_asignado = data.get('pm_asignado')
            fecha_alta = data.get('fecha_alta')
            fecha_entrega = data.get('fecha_entrega')
            costo = data.get('costo')

            proyecto = Proyecto(numero = numero, nombre=nombre, pm_asignado=pm_asignado, fecha_alta = fecha_alta,fecha_entrega = fecha_entrega, costo = costo)

            proyecto.save()

        formulario = ProyectoFormulario()
        context = {
           
            "proyectos": proyectos,
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/crear_proyecto.html", context)


    
    # if request.method == "GET":
    #     formulario = ProyectoFormulario()
    #     return render(request, "appentrega/crear_proyecto.html", {"formulario": formulario})

    # else:

    #     formulario = ProyectoFormulario(request.POST)

    #     if formulario.is_valid():
        
    #         data = formulario.cleaned_data
    #         print(data)

    #         numero = data.get("numero")
    #         nombre = data.get("nombre")
    #         pm_asignado = data.get('pm_asignado')
    #         fecha_alta = data.get('fecha_alta')
    #         costo = data.get('costo')

    #         proyecto = Proyecto(numero = numero, nombre=nombre, pm_asignado=pm_asignado, fecha_alta = fecha_alta, costo = costo)

    #         proyecto.save()

    #         return render(request, "appentrega/index.html")

    #     else:
    #         return HttpResponse("Formulario no valido") 
    

@login_required
def borrar_proyecto(request, id_proyecto):
    try:
        proyecto = Proyecto.objects.get(id=id_proyecto)        
        proyecto.delete()        

        return redirect('crear_proyecto')
       
    except:
        return redirect('inicio')

@login_required
def editar_proyecto(request, id_proyecto):

    if request.method == "GET":
        formulario = ProyectoFormulario()
        contexto = {
            "formulario": formulario
        }

        return render(request, "appentrega/componentes/editar_proyecto.html", contexto)

    else:
        formulario = ProyectoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                proyecto = Proyecto.objects.get(id=id_proyecto)
                proyecto.numero = data.get("numero")
                proyecto.nombre = data.get('nombre')
                proyecto.pm_asignado = data.get('pm_asignado')                
                proyecto.fecha_alta = data.get('fecha_alta')
                proyecto.fecha_entrega = data.get('fecha_entrega')
                proyecto.costo = data.get('costo')
                
                proyecto.save()
            except:
                return HttpResponse("Error en la actualizacion")

        return redirect('crear_proyecto')

def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()

        context = {
            "form": formulario
        }

        return render(request, "appentrega/autenticacion/login.html", context)

    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = authenticate(username=data.get(
                "username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario)
                return redirect("inicio")
            else:
                context = {
                    "error": "Credenciales no validas",
                    "form": formulario
                }
                return render(request, "appentrega/autenticacion/login.html", context)
        else:
            context = {
                "error": "Formulario NO valido",
                "form": formulario
            }
            return render(request, "appentrega/autenticacion/login.html", context)

def registrar_usuario(request):
    if request.method == "GET":
        formulario = UserCustomCreationForm()
        return render(request, "appentrega/autenticacion/registro.html", {"form": formulario})
    else:
        formulario = UserCustomCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request, "appentrega/autenticacion/registro.html", {"form": formulario, "error": "Formulario NO valido"})

@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == "GET":
        form = UserEditForm(initial={"email": request.user.email})

        return render(request, "appentrega/autenticacion/update_user.html", {"form": form})
    else:
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            try:                

                usuario.email = data['email']
                usuario.password1 = data['password1']
                usuario.password2 = data['password2']               
                usuario.save()

                return redirect("inicio")
            except:
                return HttpResponse("Error en la actualizacion")
        else:
            return render(request, "appentrega/autenticacion/update_user.html", {"form": form})

@login_required
def agregar_avatar(request):

    if request.method == "GET":
        form = AvatarForm()
        contexto = {"form": form}
        return render(request, "appentrega/autenticacion/agregar_avatar.html", contexto)
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            usuario = User.objects.filter(username=request.user.username).first()
            avatar = Avatar(usuario=usuario,imagen=data["imagen"])
            print(usuario)
            print(data)

            avatar.save()
            return redirect("inicio")
        contexto = {"form": form}
        return render(request, "appentrega/autenticacion/agregar_avatar.html", contexto)
