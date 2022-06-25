from django.db import models

# Create your models here.

class Maule(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido_mat = models.CharField(max_length=200 , verbose_name='Apellido materno')
    apellido_pat = models.CharField(max_length=200, verbose_name='Apellido paterno')
    edad = models.IntegerField()
    vacuna = models.CharField(max_length=200 , verbose_name='Nombre de Vacuna')
    fecha = models.DateField()


