from django.urls import path #importar libreria path
from .views import LolaViews #importar clase LolaViews

urlpatterns = [
    path('Lola/', LolaViews.as_view(), name='Lola_list'), #crear ruta index2
    path('Lola/<int:rut>', LolaViews.as_view(), name='companies_process2')
]
