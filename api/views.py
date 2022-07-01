from email import message #email_message
from re import I #importar libreria re
from django.http import JsonResponse #importar libreria JsonResponse
from django.shortcuts import render #importar funcion render
from django.views import View #importar clase View
from .models import Pruebas #importar tabla idusuario

# Create your views here.

class PruebasViews(View): #crear clase idusuarioViews
    def get(self, request): #crear funcion get
        Datos=list(Pruebas.objects.values()) #crear variable Datos
        if len(Datos)>0:
            datos={'message': 'Success', 'Datos': Datos} #crear variable datos
        else:
            datos={'message': 'No hay datos'}
        return JsonResponse(datos) #retornar datos

    def post(self, request): #crear funcion post
        pass
    def put(self, request): #crear funcion put
        pass
    def delete(self, request): #crear funcion delete
        pass


