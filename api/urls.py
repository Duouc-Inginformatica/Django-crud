from django.urls import path
from .views import MauleViews

urlpatterns = [
    path('', MauleViews.as_view(), name='index'),
    path('Maule/', MauleViews.as_view(), name='Maule_list'),
]
