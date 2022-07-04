from django.urls import path #importar libreria path
from .views import LolaViews #importar clase LolaViews

urlpatterns = [
    path('apilola', LolaViews.as_view(), name='index3'), #crear ruta index2
    path('index3', LolaViews.as_view(), name='index3'), #crear ruta index2
    path('Lola/', LolaViews.as_view(), name='Lola_list'), #crear ruta Lola_list
]
