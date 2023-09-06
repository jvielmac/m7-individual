from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Prioridades'


class Tarea(models.Model):
    ESTADOS_DE_TAREA = (
        ("pendiente", "Pendiente"),
        ("en_progreso", "En Progreso"),
        ("completada", "Completada")
    )

    titulo = models.CharField(max_length=70)
    descripcion = models.TextField()
    vencimiento = models.DateTimeField()
    estado = models.CharField(max_length=11, choices=ESTADOS_DE_TAREA)
    etiqueta = models.ForeignKey(Etiqueta, null=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(Prioridad, null=True, on_delete=models.SET_NULL)
    observaciones = models.TextField()

    def __str__(self):
        return self.titulo