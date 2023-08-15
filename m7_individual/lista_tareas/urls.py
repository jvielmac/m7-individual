from django.urls import path
from . import views

app_name = 'lista-tareas'

urlpatterns = [
    path('', views.index, name='main-page'),
    path('tareas/', views.bienvenida, name='listado')
]