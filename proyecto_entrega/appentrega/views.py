from django.shortcuts import render
from django.http import HttpResponse
from appentrega.models import Familiar




def familiar(request):
    familiar = Familiar(numero = 1, nombre='Luis', fecha_alta='2020-01-01')
    familiar.save()

    familiar = Familiar(numero = 2, nombre='Pedro', fecha_alta='2020-02-02')
    familiar.save()

    familiar = Familiar(numero = 3, nombre='Marta', fecha_alta='2020-03-03')
    familiar.save()

    familiares = Familiar.objects.all()

    return render(request,'appentrega/familiares.html',{'familiares': familiares})
