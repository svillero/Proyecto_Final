from django.forms import Form,CharField,IntegerField

class FormularioBusqueda(Form):
    nombre_requerimiento = CharField(max_length=50)


class RequerimientoFormulario(Form):

    numero = IntegerField()
    estado = IntegerField()
    nombre = CharField()