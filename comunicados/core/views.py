from django.shortcuts import render
from .models import Comunicado

# Create your views here.
def comunicados(request):
    comunicados = Comunicado.objects.all
    return render(request, 'core/comunicados.html', {'comunicados':comunicados})
