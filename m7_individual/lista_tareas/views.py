from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    contexto = {'usuario_activo': request.user}
    return render(request, 'lista_tareas/index.html', contexto)

@login_required()
def bienvenida(request):
    contexto = {'usuario_activo': request.user}
    return render(request, 'lista_tareas/bienvenida.html', contexto)