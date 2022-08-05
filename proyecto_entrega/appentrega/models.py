from django.db import models


class Requerimiento(models.Model):

    numero = models.IntegerField()
    estado = models.IntegerField()
    nombre = models.CharField(max_length=50)
    solicitud = models.CharField(max_length=100)
    fecha_alta = models.DateField()
    fecha_cierre = models.DateField()

class Proyecto(models.Model):

    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)
    pm_asignado = models.CharField(max_length=50)
    fecha_alta = models.DateField()
    fecha_entrega = models.DateField()
    costo = models.IntegerField()

class Cliente(models.Model):

    cliente_id = models.IntegerField()
    razon_social = models.CharField(max_length=50)
    email = models.EmailField()   
    fecha_alta = models.DateField()

class Colaborador(models.Model):

    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField()   
    fecha_alta = models.DateField()



