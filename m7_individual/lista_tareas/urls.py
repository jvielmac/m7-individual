from django.urls import path
from . import views

app_name = 'lista-tareas'

urlpatterns = [
    path('', views.Index.as_view(), name='main-page'),
    path('tareas/', views.ListadoTareas.as_view(), name='listado'),
    path('tareas/<int:pk>/', views.DetalleTarea.as_view(), name='detalle')
]