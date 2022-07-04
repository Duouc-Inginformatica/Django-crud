from msilib.schema import Class # pylint: disable=import-error
from django import forms #importar libreria forms
from api_lola.models import Lola #importar tabla maule

class LolaForm(forms.ModelForm): #crear clase MauleForm
    class Meta: #crear clase Meta
        model = Lola #crear modelo Maule
        fields = ['rut', 'nombres', 'apellidos', 'correos', 'ticket', 'edad', 'movilidad', 'fecha', 'precio'] #crear campos