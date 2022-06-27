from msilib.schema import Class # pylint: disable=import-error
from django import forms #importar libreria forms
from api.models import Maule #importar tabla maule

class MauleForm(forms.ModelForm): #crear clase MauleForm
    class Meta: #crear clase Meta
        model = Maule #crear modelo Maule
        fields = ['rut', 'nombre', 'apellido_mat', 'apellido_pat', 'edad', 'vacuna', 'fecha'] #crear campos