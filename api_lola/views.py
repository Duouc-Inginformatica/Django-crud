from email import message
import json #email_message
from re import I #importar libreria re
from django.http import HttpResponse #importar libreria http
from django.utils.decorators import method_decorator #importar libreria decorators
from django.http import JsonResponse #importar libreria JsonResponse
from django.shortcuts import render #importar funcion render
from django.views import View #importar clase View
from .models import Lola #importar tabla Lola
from django.views.decorators.csrf import csrf_exempt #importar libreria csrf_exempt

# Create your views here.

class LolaViews(View): #crear clase LolaViews
    @method_decorator(csrf_exempt) #decorar funcion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, rut=0): #crear funcion get
        if (rut > 0): #si id_usuario es mayor a 0
            Datos = list(Lola.objects.filter(rut=rut).values())
            if len(Datos) > 0:
                Dates = Datos[0]
                datos={'message': 'correcto', 'Datos': Dates}
            else:
                datos={'message': 'No hay datos!'}
        else:
            Datos=list(Lola.objects.values()) #crear variable Datos
            if len(Datos)>0:
                datos={'message': 'correcto', 'peralta': Datos} #crear variable datos
            else:
                datos={'message': 'No hay datos'}
            return JsonResponse(datos) #retornar datos


    def post(self, request): #crear funcion post
        jd = json.loads(request.body) #crear variable jd
        Lola.objects.create(correo=jd['correo'], nombre=jd['nombre'], apellido=jd['apellido'], rut=jd['rut'],pwd=jd['pwd'])
        Dates={'message': 'Datos creados!'} #crear variable dates
        return JsonResponse (Dates) #retornar Dates

        
    def put(self, request, rut):
        jd = json.loads(request.body)
        Datos = list(Lola.objects.filter(rut=rut).values())
        if len(Datos) > 0:
            Lola = Lola.objects.get(rut=rut)
            Lola.correo = jd['correo']
            Lola.nombre = jd['nombre']
            Lola.apellido = jd['apellido']
            Lola.rut = jd['rut']
            Lola.pwd = jd['pwd']
            Lola.save()
            datos = {'message': "Actualizado"}
        else:
            datos = {'message': "Lola not found..."}
        return JsonResponse(datos)

    def delete(self, request, rut): #crear funcion delete
        Datos = list(Lola.objects.filter(rut=rut).values()) 
        if len(Datos) > 0:
            Lola.objects.filter(rut=rut).delete() #crear variable Datos
            datos={'message': 'Eliminado'} #crear variable datos
        else:
            datos={'message': 'No hay datos'}
        return JsonResponse(datos) #retornar datos

