from django.shortcuts import render
from resoluciones.models import Resolucion

# Create your views here.


def home(request):
    return render(request, 'resolucion/index_p.html',
                  {'resoluciones': Resolucion.objects.count(),
                   'dato': 22})


def resolucion_list(request):
    #resoluciones = Resolucion.objects.all()
    #resoluciones = Resolucion._meta.model.objects.all()
    resoluciones = Resolucion.objects.filter(
        tipo_elevacion='Conocimiento'
    )
    return render(request, 'resolucion/resolucion_list_p.html',
                  {'resoluciones': resoluciones})


def inicio(request):
    return render(request, 'resolucion/inicio.html')


def tabla(request):
    resoluciones = Resolucion.objects.all()

    return render(request, 'resolucion/tabla.html',
                  {'resoluciones': resoluciones})






