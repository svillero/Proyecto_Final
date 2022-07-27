from django.db import models


class Familiar(models.Model):

    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha_alta = models.DateField()

