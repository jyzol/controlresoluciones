from django import forms
from .models import Resolucion, Expediente
from .models import Considerando
from .models import Resolutivo

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
        fields = ('resolucion_considerando','nro_considerando',
                  'descripcion_considerando')


class ResolutivoForm(forms.ModelForm):
    class Meta:
        model = Resolutivo
        fields = ('resolucion_resolutivo','nro_resolutivo',
                  'descripcion_resolutivo')


class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('nro_expediente','resolucion_expediente',
                  'fecha_expediente','facultad_expediente',
                  'dependencia_expediente','descripcion_expediente')








