from django import forms
from core.models import Cotizador, Trabajo, ReporteDiario, ItemCotizacion
from django.forms import ModelForm

from django.forms.models import inlineformset_factory

class CotizadorForm(ModelForm):
    class Meta:
        model = Cotizador

class TrabajoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrabajoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Trabajo
        exclude = ["user"]

class ReporteDiarioForm(ModelForm):

    def __init__(self, user=None, *args, **kwargs):
        super(ReporteDiarioForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ReporteDiario
        exclude = ["user"]
        #if user:
        #    self.fields['trabajo'].queryset = Trabajo.objects.filter(user=user)


CotizacionFormSet = inlineformset_factory(Trabajo, ItemCotizacion)
