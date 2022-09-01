from django.urls import path
from appmensajes.views import *



urlpatterns = [
    path("mensajes/", mensajes,name="mensajes")
    
    
]