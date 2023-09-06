from django.contrib import admin
from .models import Etiqueta, Tarea, Prioridad

# Register your models here.
admin.site.register(Etiqueta)
admin.site.register(Tarea)
admin.site.register(Prioridad)