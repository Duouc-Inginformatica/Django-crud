from msilib.schema import Class # pylint: disable=import-error
from django import forms #importar libreria forms
from api.models import Pruebas #importar tabla maule

class PruebasForm(forms.ModelForm): #crear clase idusuarioForm
    class Meta: #crear clase Meta
        model = Pruebas #crear modelo idusuario
        fields = ['idusuario', 'correo', 'nombre', 'apellido', 'rut', 'pwd'] #crear campos