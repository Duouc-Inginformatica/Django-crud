from re import A #importar libreria re
from django.contrib import admin #importar libreria admin
from .models import Pruebas #importar tabla idusuario

# Register your models here.

admin.site.register(Pruebas) #registrar tabla idusuario
