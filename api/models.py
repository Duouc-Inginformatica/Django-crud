from django.db import models #importar libreria models

# Create your models here.

class Maule(models.Model): #crear clase Maule
    rut = models.AutoField(primary_key=True) #crear campo rut
    nombre = models.CharField(max_length=50, verbose_name='Nombre') #crear campo nombre
    apellido_mat = models.CharField(max_length=200 , verbose_name='Apellido materno') #crear campo apellido_mat
    apellido_pat = models.CharField(max_length=200, verbose_name='Apellido paterno') #crear campo apellido_pat
    edad = models.IntegerField() #crear campo edad
    vacuna = models.CharField(max_length=200 , verbose_name='Nombre de Vacuna') #crear campo vacuna
    fecha = models.DateField() #crear campo fecha


