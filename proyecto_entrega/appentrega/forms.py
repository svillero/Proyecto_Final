from django.forms import Form,CharField,IntegerField,DateField,EmailField

class FormularioBusqueda(Form):
    nombre_requerimiento = CharField(max_length=50)


class RequerimientoFormulario(Form):

    numero = IntegerField()
    estado = IntegerField()
    nombre = CharField()
    solicitud = CharField()
    fecha_alta = DateField()

class ProyectoFormulario(Form):

    numero = IntegerField()
    nombre = CharField()
    pm_asignado = CharField()
    fecha_alta = DateField()
    fecha_entrega = DateField()
    costo = IntegerField()


class ClienteFormulario(Form):

    cliente_id = IntegerField()
    razon_social = CharField()
    email = EmailField()
    fecha_alta = DateField()
   


class ColaboradorFormulario(Form):

    numero = IntegerField()
    nombre = CharField()
    apellido = CharField()
    cargo = CharField()
    email = EmailField()
    fecha_alta = DateField()
  


 