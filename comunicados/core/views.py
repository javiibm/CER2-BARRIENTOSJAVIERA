from django.shortcuts import render, redirect
from .models import Comunicado
from .models import Categoria

# Create your views here.

def comunicados(request):
    comunicados = Comunicado.objects.order_by('-fecha_envio')
    categorias = Categoria.objects.all()
    diccionarios = {'comunicados':comunicados, 'categorias':categorias}

    getniveles = request.GET.get('btn.value')
    getcategorias= request.GET.get('categoria')

    if getniveles:
        comunicados = comunicados.filter(nivel=getniveles)
        

    if getcategorias:
        comunicados = comunicados.filter(categoria_id=getcategorias)
        
    return render(request, 'core/comunicados.html', diccionarios)



