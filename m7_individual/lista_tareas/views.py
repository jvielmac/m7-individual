from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
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
        estado = self.request.GET.get('estado')
        etiqueta = self.request.GET.get('etiqueta')

        if estado:
            kwargs_filter['estado'] = estado

        if etiqueta:
            kwargs_filter['etiqueta'] = int(etiqueta)

        return Tarea.objects.filter(**kwargs_filter).order_by('vencimiento')

class DetalleTarea(LoginRequiredMixin, UsuarioMixin, generic.DetailView):
    template_name = 'lista_tareas/detalle.html'
    model = Tarea
    context_object_name = 'tarea'

class CrearTarea(LoginRequiredMixin, UsuarioMixin, generic.CreateView):
    template_name = 'lista_tareas/editar_tarea.html'
    model = Tarea
    fields = [
        'titulo',
        'descripcion',
        'vencimiento',
        'estado',
        'etiqueta',
    ]
    extra_context = {'texto_submit': 'Crear'}
    success_url = reverse_lazy('lista-tareas:listado')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class EditarTarea(LoginRequiredMixin, UsuarioMixin, generic.UpdateView):
    template_name = 'lista_tareas/editar_tarea.html'
    model = Tarea
    fields = [
        'titulo',
        'descripcion',
        'vencimiento',
        'estado',
        'etiqueta',
    ]
    extra_context = {'texto_submit': 'Editar'}

    def get_success_url(self):
        return reverse('lista-tareas:detalle', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)