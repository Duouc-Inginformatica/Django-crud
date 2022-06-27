from django.urls import path #importar libreria path
from .views import PruebasViews #importar clase idusuarioViews

urlpatterns = [
    path('api', PruebasViews.as_view(), name='index2'), #crear ruta index2
    path('index2', PruebasViews.as_view(), name='index2'), #crear ruta index2
    path('idusuario/', PruebasViews.as_view(), name='Prueba_list'), #crear ruta idusuario_list
]
