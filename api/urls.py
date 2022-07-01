from django.urls import path #importar libreria path
from .views import PruebasViews #importar clase idusuarioViews

urlpatterns = [
    path('Datos/', PruebasViews.as_view(), name='Datos_list'), #crear ruta index2
    path('Datos/<int:idusuario>', PruebasViews.as_view(), name='companies_process')]
