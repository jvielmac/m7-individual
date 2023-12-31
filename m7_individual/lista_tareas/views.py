from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from .models import Tarea
from .forms import FiltrarForm
from utils.mixins import UsuarioMixin

# Create your views here.

class Index(UsuarioMixin, generic.TemplateView):
    template_name = 'lista_tareas/index.html'
    http_method_names = ['get']


class ListadoTareas(LoginRequiredMixin, UsuarioMixin, generic.ListView):
    template_name = 'lista_tareas/listado.html'
    context_object_name = 'tareas'
    extra_context = {'filtrar_form': FiltrarForm}

    def get_queryset(self):
        kwargs_filter = {'usuario': self.request.user.pk}
        filtros = ['estado', 'etiqueta', 'prioridad']

        for clave_filtro in filtros:
            valor_filtro = self.request.GET.get(clave_filtro)

            if valor_filtro:
                kwargs_filter[clave_filtro] = valor_filtro

        return Tarea.objects.filter(**kwargs_filter).order_by('vencimiento')


class DetalleTarea(LoginRequiredMixin, UsuarioMixin, generic.DetailView, generic.UpdateView):
    template_name = 'lista_tareas/detalle.html'
    model = Tarea
    context_object_name = 'tarea'
    fields = ['observaciones']

    def get_success_url(self):
        return reverse('lista-tareas:detalle', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class CrearTarea(LoginRequiredMixin, UsuarioMixin, generic.CreateView):
    template_name = 'lista_tareas/editar_tarea.html'
    model = Tarea
    fields = [
        'titulo',
        'descripcion',
        'vencimiento',
        'estado',
        'etiqueta',
        'usuario',
        'prioridad',
    ]
    extra_context = {'texto_submit': 'Crear'}
    success_url = reverse_lazy('lista-tareas:listado')


class EditarTarea(LoginRequiredMixin, UsuarioMixin, generic.UpdateView):
    template_name = 'lista_tareas/editar_tarea.html'
    model = Tarea
    fields = [
        'titulo',
        'descripcion',
        'vencimiento',
        'estado',
        'etiqueta',
        'prioridad',
    ]
    extra_context = {'texto_submit': 'Editar'}

    def get_success_url(self):
        return reverse('lista-tareas:detalle', kwargs={'pk': self.object.pk})


class EliminarTarea(LoginRequiredMixin, UsuarioMixin, generic.DeleteView):
    template_name = 'lista_tareas/eliminar_tarea.html'
    model = Tarea
    success_url = reverse_lazy('lista-tareas:listado')

    def form_valid(self, form):
        if self.request.user != self.object.usuario:
            return HttpResponseForbidden("<h1>403: No tienes permitido realizar esta operación</h1>")

        return super().form_valid(form)


class CompletarTarea(LoginRequiredMixin, UsuarioMixin, generic.UpdateView):
    http_method_names = ['post']
    model = Tarea
    fields = ['estado']
    success_url = reverse_lazy('lista-tareas:listado')

    def form_valid(self, form):
        if self.request.user != self.object.usuario:
            return HttpResponseForbidden("<h1>403: No tienes permitido realizar esta operación</h1>")

        return super().form_valid(form)