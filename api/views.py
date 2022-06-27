from email import message #email_message
from re import I #importar libreria re
from django.http import JsonResponse #importar libreria JsonResponse
from django.shortcuts import render #importar funcion render
from django.views import View #importar clase View
from .models import Pruebas #importar tabla idusuario

# Create your views here.

class PruebasViews(View): #crear clase idusuarioViews
    def get(self, request): #crear funcion get
        return render(request, 'index.html') #enviar datos a la pagina index.html

    def post(self, request):    #crear funcion post
        return render(request, 'index.html') #enviar datos a la pagina index.html
    
    def put(self, request): #crear funcion put
        return render(request, 'index.html') #enviar datos a la pagina index.html

    def delete(self, request): #crear funcion delete
        return render(request, 'index.html') #enviar datos a la pagina index.html

