from django.contrib import admin
from .models import *


# Register your models here.

class ResolucionAdmin(admin.ModelAdmin):
    list_display = ('nro_resolucion', 'facultad_resolucion',
                    'fecha_resolucion', 'descripcion_resolucion')
    list_filter = ('facultad_resolucion','tipo_elevacion')
    search_fields = ('descripcion_resolucion','facultad_resolucion')
    date_hierarchy = 'fecha_resolucion'
    ordering = ['fecha_resolucion','facultad_resolucion']


admin.site.register(Facultad)
admin.site.register(Dependencia)
admin.site.register(Resolucion, ResolucionAdmin)
admin.site.register(Resolutivo)
admin.site.register(Considerando)
admin.site.register(Persona)
admin.site.register(Expediente)
