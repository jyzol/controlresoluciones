from django.shortcuts import render
from resoluciones.models import Resolucion

# Create your views here.


def home(request):
    return render(request, 'resolucion/index.html',
                  {'resoluciones': Resolucion.objects.count(),
                   'dato': 22})


def resolucion_list(request):
    #resoluciones = Resolucion.objects.all()
    #resoluciones = Resolucion._meta.model.objects.all()
    resoluciones = Resolucion.objects.filter(
        tipo_elevacion='Conocimiento'
    )
    return render(request, 'resolucion/index.html',
                  {'resoluciones': resoluciones})






