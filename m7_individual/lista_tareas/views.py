from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from .models import Tarea
from utils.mixins import UsuarioMixin

# Create your views here.

class Index(UsuarioMixin, TemplateView):
    template_name = 'lista_tareas/index.html'
    http_method_names = ['get']

class ListadoTareas(LoginRequiredMixin, UsuarioMixin, ListView):
    template_name = 'lista_tareas/listado.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        tareas_usuario = Tarea.objects.filter(usuario=self.request.user.pk)
        return tareas_usuario.order_by('vencimiento')

class DetalleTarea(LoginRequiredMixin, UsuarioMixin, DetailView):
    template_name = 'lista_tareas/detalle.html'
    model = Tarea
    context_object_name = 'tarea'