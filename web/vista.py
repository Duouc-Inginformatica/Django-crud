import re  #importar libreria re
from tkinter import EW #importar libreria tkinter
from django.shortcuts import redirect, render #importar funciones redirect y render
from api.models import Maule #importar la tabla maule
from api.forms import MauleForm #importar formulario


# enviar datos a la tabla
def index(request): #crear funcion index
    Maules = Maule.objects.all() #crear variable maules y llamar a la tabla maule
    return render(request, 'index.html', {'Maules': Maules}) #enviar datos a la pagina index.html en variable maules

# eliminar datos de la tabla
def eliminar(request, rut): #crear funcion eliminar
    remover = Maule.objects.get(rut=rut) #crear variable remover y llamar a la tabla maule
    remover.delete() #eliminar datos de la tabla
    return redirect('index') #redireccionar a la pagina index.html

# eliminar datos de la tabla
def registrar(request): #crear funcion registrar
    rut = request.POST.get('rut') #crear variable rut y llamar a la variable rut de la pagina index.html
    nombre = request.POST.get('nombre') #crear variable nombre y llamar a la variable nombre de la pagina index.html
    apellido_mat = request.POST.get('apellido_mat') #crear variable apellido_mat y llamar a la variable apellido_mat de la pagina index.html
    apellido_pat = request.POST.get('apellido_pat') #crear variable apellido_pat y llamar a la variable apellido_pat de la pagina index.html
    edad = request.POST.get('edad') #crear variable edad y llamar a la variable edad de la pagina index.html
    vacuna = request.POST.get('vacuna') #crear variable vacuna y llamar a la variable vacuna de la pagina index.html
    fecha = request.POST.get('fecha') #crear variable fecha y llamar a la variable fecha de la pagina index.html
    registro=Maule.objects.create(rut=rut, nombre=nombre, apellido_mat=apellido_mat, apellido_pat=apellido_pat, edad=edad, vacuna=vacuna, fecha=fecha) #crear variable registro y llamar a la tabla maule
    return redirect('index') #redireccionar a la pagina index.html