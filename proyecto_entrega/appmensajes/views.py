from django.shortcuts import render

# Create your views here.
from asyncio.windows_events import NULL
from operator import is_not
from django.shortcuts import render, redirect
from appmensajes.models import Mensaje
from appmensajes.forms import MensajeFormulario
from datetime import datetime


def mensajes(request):   

    usu = request.user
    
    mensajes = Mensaje.objects.all()

    if request.method == "GET":
        formulario = MensajeFormulario()
        context = {
            
            "mensajes": mensajes,
            "formulario": formulario
        }

        return render(request, "appmensajes/mensajes.html", context)

    else:

        formulario = MensajeFormulario(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
            print(data)

            texto = data.get('texto')            
            fecha_alta = datetime.now()
            usuario = usu.username
            
            

            mensaje = Mensaje(texto = texto, fecha_alta = fecha_alta,usuario =usuario  )
            mensaje.save()        

        formulario = MensajeFormulario()
        context = {
           
            "mensajes": mensajes,
            "formulario": formulario
        }

        return render(request, "appmensajes/mensajes.html", context)

