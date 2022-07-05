from django.urls import path #importar libreria path
from .views import MauleViews #importar clase MauleViews

urlpatterns = [
    path('Datos/', MauleViews.as_view(), name='Datos_list'), #crear ruta index2
    path('Datos/<int:rut>', MauleViews.as_view(), name='companies_process')
]
