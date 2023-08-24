from django.urls import path
from . import views

app_name = 'lista-tareas'

urlpatterns = [
    path('', views.Index.as_view(), name='main-page'),
    path('tareas/', views.ListadoTareas.as_view(), name='listado'),
    path('tareas/<int:pk>/', views.DetalleTarea.as_view(), name='detalle'),
    path('tareas/crear/', views.CrearTarea.as_view(), name='crear'),
    path('tareas/<int:pk>/editar', views.EditarTarea.as_view(), name='editar'),
    path('tareas/<int:pk>/eliminar', views.EliminarTarea.as_view(), name='eliminar'),
    path('tareas/<int:pk>/completar', views.CompletarTarea.as_view(), name='completar'),
]