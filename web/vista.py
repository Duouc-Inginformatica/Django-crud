import re
from tkinter import EW
from django.shortcuts import redirect, render
from api.models import Maule
from api.forms import MauleForm


# enviar datos a la tabla
def index(request):
    Maules = Maule.objects.all()
    return render(request, 'index.html', {'Maules': Maules})


def eliminar(request, rut):
    remover = Maule.objects.get(rut=rut)
    remover.delete()
    return redirect('index')

def registrar(request):
    rut = request.POST.get('rut')
    nombre = request.POST.get('nombre')
    apellido_mat = request.POST.get('apellido_mat')
    apellido_pat = request.POST.get('apellido_pat')
    edad = request.POST.get('edad')
    vacuna = request.POST.get('vacuna')
    fecha = request.POST.get('fecha')
    registro=Maule.objects.create(rut=rut, nombre=nombre, apellido_mat=apellido_mat, apellido_pat=apellido_pat, edad=edad, vacuna=vacuna, fecha=fecha)
    return redirect('index')