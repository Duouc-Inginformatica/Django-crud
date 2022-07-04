from importlib.resources import contents
import re  #importar libreria re
from tkinter import EW #importar libreria tkinter
from django.shortcuts import redirect, render #importar funciones redirect y render
from api.models import Maule #importar la tabla maule
from api.forms import MauleForm #importar formulario

from api_lola.models import Lola #importar la tabla maule
from api_lola.forms import LolaForm #importar formulario


# enviar datos a la tabla
def index(request): #crear funcion index
    Maules = Maule.objects.all() #crear variable maules y llamar a la tabla maule
    return render(request, 'index.html', {'Maules': Maules}) #enviar datos a la pagina index.html en variable maules

def homies(request): #crear funcion index
    return render(request, 'homies.html') #enviar datos a la pagina index.html en variable litio

def form2(request): #crear funcion index
    litio = Lola.objects.all() #crear variable litio y llamar a la tabla lola
    return render(request, 'form2.html', {'litio': litio}) #enviar datos a la pagina index.html en variable litio

# eliminar datos de la tabla
def eliminar(request, rut): #crear funcion eliminar
    remover = Maule.objects.get(rut=rut) #crear variable remover y llamar a la tabla maule
    remover.delete() #eliminar datos de la tabla
    return redirect('index') #redireccionar a la pagina index.html

# eliminar datos de la tabla
def eliminare(request, rut): #crear funcion eliminar
    removere = Lola.objects.get(rut=rut) #crear variable remover y llamar a la tabla maule
    removere.delete() #eliminar datos de la tabla
    return redirect('form2') #redireccionar a la pagina index.html

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

# eliminar datos de la tabla
def registrare(request): #crear funcion registrar
    rut = request.POST.get('rut') #crear variable rut y llamar a la variable rut de la pagina index.html
    nombres = request.POST.get('nombres') #crear variable nombres y llamar a la variable nombres de la pagina index.html
    apellidos = request.POST.get('apellidos') #crear variable apellidos y llamar a la variable apellidos de la pagina index.html
    correos = request.POST.get('correos') #crear variable correo y llamar a la variable correo de la pagina index.html
    ticket = request.POST.get('ticket') #crear variable ticket y llamar a la variable ticket de la pagina index.html
    edad = request.POST.get('edad') #crear variable edad y llamar a la variable edad de la pagina index.html
    fecha = request.POST.get('fecha') #crear variable fecha y llamar a la variable fecha de la pagina index.html
    datala = Lola.objects.create(rut=rut, nombres=nombres, apellidos=apellidos, correos=correos, ticket=ticket, edad=edad, fecha=fecha) #crear variable registro y llamar a la tabla maule
    return redirect('form2') #redireccionar a la pagina index.html


#django editar datos de la tabla
def editar(request, rut): #crear funcion editar
    obj = Maule.objects.get(rut=rut) #crear variable obj y llamar a la tabla maule
    if request.method == 'GET': #si el metodo es get
        form = MauleForm(instance=obj) #crear variable form y llamar a la variable obj de la tabla maule
    else: 
        form = MauleForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'editar.html', {'form': form})
        return render(request, 'editar.html', {'form': form}) #enviar datos a la pagina editar.html en variable form