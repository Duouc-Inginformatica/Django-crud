from django.shortcuts import redirect, render
from api.models import Maule
from api.forms import MauleForm


# enviar datos a la tabla
def index(request):
    Maules = Maule.objects.all()
    return render(request, 'index.html', {'Maules': Maules})


def eliminar(request, rut):
    remover = Maule.objects.get(rut=rut)
    remover.delete()
    return redirect('index.html')