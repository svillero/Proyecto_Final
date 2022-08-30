from django.forms import Form, IntegerField, CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

    rut = IntegerField()
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

class UserCustomCreationForm(UserCreationForm):

    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { "username": "No mas de 20 caracteres", "email": "", "password1": "", "password2": "" }
  


 