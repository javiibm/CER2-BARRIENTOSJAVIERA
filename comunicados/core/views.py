from django.shortcuts import render, redirect
from .models import Comunicado

# Create your views here.
def comunicados(request):
    comunicados = Comunicado.objects.order_by('-fecha_envio')
    return render(request, 'core/comunicados.html', {'comunicados':comunicados})

