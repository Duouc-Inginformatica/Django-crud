from django.db import models #importar libreria models

# Create your models here.

class Lola(models.Model): #crear clase Maule
    rut = models.AutoField(primary_key=True) #crear campo rut
    nombres = models.CharField(max_length=50, verbose_name='Nombre') #crear campo nombre
    apellidos = models.CharField(max_length=200 , verbose_name='Apellido materno') #crear campo apellido_mat
    correos = models.EmailField(max_length=200, verbose_name='Correo') #crear campo correo
    ticket = models.CharField(max_length=200, verbose_name='Ticket') #crear campo ticket
    edad = models.IntegerField() #crear campo edad
    movilidad = models.CharField(max_length=200, verbose_name='Movilidad') #crear campo movilidad
    fecha = models.DateField() #crear campo fecha
    precio = models.IntegerField() #crear campo precio

