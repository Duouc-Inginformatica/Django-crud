import re  #importar libreria re
from tkinter import EW
from urllib.request import Request #importar libreria tkinter
from django.shortcuts import redirect, render #importar funciones redirect y render
from api.models import Pruebas #importar la tabla PRUEBAS
from api.forms import PruebasForm #importar formulario


# enviar datos a la tabla
def index(request): #crear funcion index
    Sistema = Pruebas.objects.all() #crear variable PRUEBAS y llamar a la tabla PRUEBAS
    return render(request, 'index.html', {'Sistema': Sistema}) #enviar datos a la pagina index.html en variable PRUEBAS

# eliminar datos de la tabla
def eliminar(request, idusuario): #crear funcion eliminar
    remover = Pruebas.objects.get(idusuario=idusuario) #crear variable remover y llamar a la tabla PRUEBAS
    remover.delete() #eliminar datos de la tabla
    return redirect('index') #redireccionar a la pagina index.html
#---------------------------------------------------------------------------------------------------------------------

# escribir datos en la tabla

def registrar(request):
    # idusuario = request.POST.get('idusuario') #crear variable idusuario y llamar a la variable idusuario de la pagina registrar.html
    correo = request.POST.get('correo') #crear variable correo y llamar a la variable correo de la pagina registrar.html
    nombre = request.POST.get('nombre') #crear variable nombre y llamar a la variable nombre de la pagina registrar.html
    apellido = request.POST.get('apellido') #crear variable apellido y llamar a la variable apellido de la pagina registrar.html
    rut = request.POST.get('rut') #crear variable rut y llamar a la variable rut de la pagina registrar.html
    pwd = request.POST.get('pwd') #crear variable pwd y llamar a la variable pwd de la pagina registrar.html
    Pruebas.objects.create(correo=correo, nombre=nombre, apellido=apellido, rut=rut, pwd=pwd) #crear datos en la tabla
    return redirect('index') #redireccionar a la pagina index.html