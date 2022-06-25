from msilib.schema import Class
from django import forms
from api.models import Maule

class MauleForm(forms.ModelForm):
    class Meta:
        model = Maule
        fields = ['rut', 'nombre', 'apellido_mat', 'apellido_pat', 'edad', 'vacuna', 'fecha']