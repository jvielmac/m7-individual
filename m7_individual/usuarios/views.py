from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def usuario_logout(request):
    logout(request)
    return redirect('lista-tareas:main-page')