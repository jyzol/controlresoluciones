from django import forms
from .models import Resolucion
from .models import Considerando

class ResolucionForm(forms.ModelForm):
    class Meta:
        model = Resolucion
        fields = ('nro_resolucion','facultad_resolucion',
                  'fecha_resolucion','link_descarga',
                  'estado_resolucion','descripcion_resolucion',
                  'observacion_resolucion','adjunto_resolucion',
                  'tipo_elevacion')


class ConsiderandoForm(forms.ModelForm):
    class Meta:
        model = Considerando
        fields = ('nro_considerando','descripcion_considerando')






