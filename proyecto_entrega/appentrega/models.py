from django.db import models
from django.contrib.auth.models import User


class Requerimiento(models.Model):

    numero = models.IntegerField()
    estado = models.IntegerField()
    nombre = models.CharField(max_length=50)
    solicitud = models.CharField(max_length=100)
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    def __str__(self):
        return f'{self.nombre}'

class Proyecto(models.Model):

    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)
    pm_asignado = models.CharField(max_length=50)
    fecha_alta = models.DateField()
    fecha_entrega = models.DateField(blank=True, null=True)
    costo = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.numero} - {self.nombre}'

class Cliente(models.Model):

    rut = models.IntegerField()
    razon_social = models.CharField(max_length=50)
    email = models.EmailField()   
    fecha_alta = models.DateField()
    
    def __str__(self):
        return f'{self.rut} - {self.razon_social}'

class Colaborador(models.Model):

    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField()   
    fecha_alta = models.DateField()

    
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'


class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

