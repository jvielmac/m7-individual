from django import forms
from .models import Tarea, Etiqueta, Prioridad

class FiltrarForm(forms.Form):
    ESTADOS = (("", "(Cualquiera)"), *Tarea.ESTADOS_DE_TAREA)

    estado = forms.ChoiceField(choices=ESTADOS, required=False)
    etiqueta = forms.ModelChoiceField(Etiqueta.objects, required=False)
    prioridad = forms.ModelChoiceField(Prioridad.objects, required=False)


class ObservacionesForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ("observaciones",)