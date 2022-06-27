from django.urls import path #importar libreria path
from .views import MauleViews #importar clase MauleViews

urlpatterns = [
    path('api', MauleViews.as_view(), name='index2'), #crear ruta index2
    path('index2', MauleViews.as_view(), name='index2'), #crear ruta index2
    path('Maule/', MauleViews.as_view(), name='Maule_list'), #crear ruta Maule_list
]
