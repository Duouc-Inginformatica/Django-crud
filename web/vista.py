from django.shortcuts import render
from api.models import Maule

# enviar datos a la tabla
def index(request):
    Maules = Maule.objects.all()
    return render(request, 'index.html', {'Maules': Maules})