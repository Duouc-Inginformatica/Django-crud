from xml.etree.ElementInclude import include as include_xml #para incluir archivos xml
from django.contrib import admin #para que se pueda usar el admin
from django.urls import path,include #para incluir las urls de otra app
from web.vista import index, eliminar, registrar, editar, homies #para incluir las urls de la app web

urlpatterns = [ #crear urls
    path('admin/', admin.site.urls), #para que se pueda acceder a la pagina de admin
    path('', homies, name='home'), #para que se pueda acceder a la pagina de index
    path('homies.html', homies, name='home_homies'), #para que se pueda acceder a la pagina de index
    path('index', index, name='index'), #para que se pueda acceder a la pagina de index
    path('api/', include('api.urls')), #para que se pueda acceder a la pagina de api
    path('eliminar/<rut>', eliminar, name='eliminar'), #para que se pueda acceder a la pagina de eliminar
   path('registrar', registrar, name='registrar'), #para que se pueda acceder a la pagina de registrar
    path('editar/<rut>', editar, name='editar'), #para que se pueda acceder a la pagina de editar
]
