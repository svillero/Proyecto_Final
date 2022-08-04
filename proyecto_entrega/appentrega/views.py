from django.shortcuts import render
from django.http import HttpResponse
from appentrega.models import Familiar




def inicio(request):

    return render(request,'appentrega/index.html',{"mensaje": "Testing"})
