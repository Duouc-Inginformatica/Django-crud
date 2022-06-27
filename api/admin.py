from re import A #importar libreria re
from django.contrib import admin #importar libreria admin
from .models import Maule #importar tabla maule

# Register your models here.

admin.site.register(Maule) #registrar tabla Maule
