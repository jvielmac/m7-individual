from django import forms
from .models import Tarea, Etiqueta

class FiltrarForm(forms.Form):
    ESTADOS = (("", "(Cualquiera)"), *Tarea.ESTADOS_DE_TAREA)

    estado = forms.ChoiceField(choices=ESTADOS, required=False)
    etiqueta = forms.ModelChoiceField(Etiqueta.objects, required=False)


class ObservacionesForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ("observaciones",)