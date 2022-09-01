from django.db import models

# Create your models here.
class Mensaje(models.Model):
    
    texto = models.CharField(max_length=300, null=True)    
    fecha_alta = models.DateTimeField(blank=True, null=True)    
    usuario = models.CharField(max_length=70, null=True)  
        
    def __str__(self):
        return f'{self.texto}'