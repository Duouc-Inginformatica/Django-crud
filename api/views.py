from email import message
import json #email_message
from re import I #importar libreria re
from django.http import HttpResponse #importar libreria http
from django.utils.decorators import method_decorator #importar libreria decorators
from django.http import JsonResponse #importar libreria JsonResponse
from django.shortcuts import render #importar funcion render
from django.views import View #importar clase View
from .models import Pruebas #importar tabla idusuario
from django.views.decorators.csrf import csrf_exempt #importar libreria csrf_exempt
import json #importar libreria json

# Create your views here.

class PruebasViews(View): #crear clase idusuarioViews

    @method_decorator(csrf_exempt) #decorar funcion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request): #crear funcion get
        Datos=list(Pruebas.objects.values()) #crear variable Datos
        if len(Datos)>0:
            datos={'message': 'Success', 'Datos': Datos} #crear variable datos
        else:
            datos={'message': 'No hay datos'}
        return JsonResponse(datos) #retornar datos


    def post(self, request): #crear funcion post
        jd = json.loads(request.body) #crear variable jd
        Pruebas.objects.create(correo=jd['correo'], nombre=jd['nombre'], apellido=jd['apellido'], rut=jd['rut'],pwd=jd['pwd'])
        Dates={'message': 'Success'} #crear variable dates
        return JsonResponse (Dates) #retornar Dates

        
    def put(self, request): #crear funcion put
        pass
    def delete(self, request): #crear funcion delete
        pass


