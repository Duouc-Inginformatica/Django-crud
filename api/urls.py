from django.urls import path
from .views import MauleViews

urlpatterns = [
    path('api', MauleViews.as_view(), name='index2'),
    path('index2', MauleViews.as_view(), name='index2'),
    path('Maule/', MauleViews.as_view(), name='Maule_list'),
]
