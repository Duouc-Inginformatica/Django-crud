from django.db import models #importar libreria models

# Create your models here.

class Pruebas(models.Model): #crear clase idusuario
    idusuario=models.AutoField(primary_key=True) #crear campo idusuario
    #correo requiere de EmailField
    correo=models.EmailField(max_length=100, verbose_name='Correo') #crear campo correo
    nombre= models.CharField(max_length=15, verbose_name='Nombre') #crear campo nombre
    apellido= models.CharField(max_length=15, verbose_name='Apellido') #crear campo apellido
    rut=models.CharField(max_length=15) #crear campo rut
    pwd=models.CharField(max_length=30)


