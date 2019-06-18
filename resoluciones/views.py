from django.shortcuts import render, redirect

from resoluciones.forms import *
from resoluciones.models import *

# Create your views here.

def inicio(request):
    return render(request, 'resolucion/inicio.html')


def tablaresolucion(request):
    resoluciones = Resolucion.objects.all()
    return render(request, 'resolucion/tablaresolucion.html',
                  {'resoluciones': resoluciones})

def nuevoresolucion(request):
    if request.method == "POST":
        form = ResolucionForm(request.POST)
        if form.is_valid():
            resolucion = form.save(commit=False)
            resolucion.save()
            return redirect('tablaresolucion')
    else:
        form = ResolucionForm

    return render(request, 'resolucion/nuevoresolucion.html', {'form':form})

def editarresolucion(request):
    if request.method == "POST":
        form = ResolucionForm(request.POST)
        #post_nro = request.POST['nro']
        #post_nro = request.POST.get('nro',False)
        if request.POST.get('nro',False) is not None:
                try:
                    post_nro = request.POST.get('nro',False)
                    res = Resolucion.objects.get(nro_resolucion=post_nro)
                    form.fields['nro_resolucion'].initial = res.nro_resolucion
                    form.fields['facultad_resolucion'].initial = res.facultad_resolucion
                    form.fields['fecha_resolucion'].initial = res.fecha_resolucion.strftime("%Y-%m-%d")
                    form.fields['link_descarga'].initial = res.link_descarga
                    form.fields['estado_resolucion'].initial = res.estado_resolucion
                    form.fields['adjunto_resolucion'].initial = res.adjunto_resolucion
                    form.fields['tipo_elevacion'].initial = res.tipo_elevacion
                except Resolucion.DoesNotExist:
                    res = None
                if form.is_valid():
                    resolucion = form
                    resolucion.save()
                    return redirect('tablaresolucion')
    else:
        form = ResolucionForm

    return render(request,'resolucion/editarresolucion.html',{'form':form, 'res':res},)

def eliminarresolucion(request):
    post_nro = '00000'
    if request.method == "POST":
        postt = request.POST['nro']
        if postt is not None:
                try:
                    res = Resolucion.objects.get(nro_resolucion=postt)
                    res.delete()
                except Resolucion.DoesNotExist:
                    res = None
        return redirect('tablaresolucion')
    else:
        return redirect('tablaresolucion')

    #return render(request, 'resolucion/eliminarresolucion.html')


'considerando'
def tablaconsiderando(request):
    considerandos = Considerando.objects.all()
    return render(request, 'resolucion/tablaconsiderando.html',
                  {'considerandos': considerandos})


def nuevoconsiderando(request):
    return render(request,'resolucion/nuevoconsiderando.html')


def editarconsiderando(request):
    return render(request,'resolucion/editarconsiderando.html')


'resolutivo'
def tablaresolutivo(request):
    resolutivos = Resolutivo.objects.all()
    return render(request, 'resolucion/tablaresolutivo.html',
                  {'resolutivos': resolutivos})


def nuevoresolutivo(request):
    return render(request,'resolucion/nuevoresolutivo.html')


def editarresolutivo(request):
    return render(request,'resolucion/editarconsiderando.html')


'dependencia'
def tabladependencia(request):
    dependencias = Dependencia.objects.all()
    return render(request, 'resolucion/tabladependencia.html',
                  {'dependencias': dependencias})


def nuevodependencia(request):
    return render(request,'resolucion/nuevodependencia.html')


def editardependencia(request):
    return render(request,'resolucion/editardependencia.html')


'expediente'
def tablaexpediente(request):
    expedientes = Expediente.objects.all()
    return render(request, 'resolucion/tablaexpediente.html',
                  {'expedientes': expedientes})


def nuevoexpediente(request):
    return render(request,'resolucion/nuevoexpediente.html')


def editarexpediente(request):
    return render(request,'resolucion/editarexpediente.html')


'facultad'
def tablafacultad(request):
    facultades = Facultad.objects.all()
    return render(request, 'resolucion/tablafacultad.html',
                  {'facultades': facultades})

'persona'
def tablapersona(request):
    personas = Persona.objects.all()
    return render(request, 'resolucion/tablapersona.html',
                  {'personas': personas})


def nuevopersona(request):
    return render(request,'resolucion/nuevopersona.html')


def editarpersona(request):
    return render(request,'resolucion/editarpersona.html')


