from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView

from resoluciones.forms import *
from resoluciones.models import *

# Create your views here.

def inicio(request):
    return render(request, 'resolucion/inicio.html')


def tablaresolucion(request):
    resoluciones = Resolucion.objects.all()
    resolutivos = Resolutivo.objects.all()
    considerandos = Considerando.objects.all()
    expedientes = Expediente.objects.all()
    dependencias = Dependencia.objects.all()
    personas = Persona.objects.all()
    return render(request, 'resolucion/tablaresolucion.html',
                  {'resoluciones': resoluciones,'resolutivos':resolutivos,'considerandos':considerandos,
                   'expedientes':expedientes,'dependencias':dependencias,'personas':personas})


def detalleresolucion(request):
    if request.method == "POST":
        post_nro = request.POST.get('nro',False)
        if post_nro is not None:
                try:
                    resolucion = Resolucion.objects.get(nro_resolucion=post_nro)
                    considerando = Considerando.objects.filter(resolucion_considerando=resolucion)
                    expediente = Expediente.objects.filter(resolucion_expediente=resolucion)
                    resolutivo = Resolutivo.objects.filter(resolucion_resolutivo=resolucion)
                    persona = Persona.objects.filter(resoluciones=resolucion)
                except Resolucion.DoesNotExist:
                    resolucion = None
    else:
        resolucion = None

    return render(request, 'resolucion/detalleresolucion.html',
                  {'resolucion':resolucion,'considerando':considerando,'expediente':expediente,'resolutivo':resolutivo,
                   'persona':persona})


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
        post_nro = request.POST.get('nro',False)
        if post_nro is not None:
                try:
                    res = Resolucion.objects.get(nro_resolucion=post_nro)
                    res.fecha_resolucion = res.fecha_resolucion.strftime("%Y-%m-%d")
                except Resolucion.DoesNotExist:
                    res = None
    else:
        form = ResolucionForm

    return render(request,'resolucion/editarresolucion.html',{'form':form, 'res':res},)


def resolucionedit(request):
    if request.method == "POST":
        post_nro = request.POST.get('nro_resolucion',False)
        res = Resolucion.objects.get(nro_resolucion=post_nro)
        res.nro_resolucion = request.POST.get('nro_resolucion',False)
        res.facultad_resolucion = Facultad.objects.get(id_facultad=request.POST.get('facultad_resolucion',False))
        res.fecha_resolucion = request.POST.get('fecha_resolucion',False)
        res.link_descarga = request.POST.get('link_descarga',False)
        res.estado_resolucion = request.POST.get('estado_resolucion',False)
        res.descripcion_resolucion = request.POST.get('descripcion_resolucion',False)
        res.observacion_resolucion = request.POST.get('observacion_resolucion', False)
        res.adjunto_resolucion = request.POST.get('adjunto_resolucion', False)
        res.tipo_elevacion = request.POST.get('tipo_elevacion', False)
        res.save()
        return redirect('tablaresolucion')

    return render(request, 'resolucion/editarresolucion.html',)


def eliminarresolucion(request):
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


'considerando'
def tablaconsiderando(request):
    considerandos = Considerando.objects.all()
    return render(request, 'resolucion/tablaconsiderando.html',
                  {'considerandos': considerandos})


def nuevoconsiderando(request):
    if request.method == "POST":
        form = ConsiderandoForm(request.POST)
        if form.is_valid():
            considerando = form.save(commit=False)
            considerando.save()
            return redirect('tablaresolucion')
    else:
        form = ConsiderandoForm

    return render(request, 'resolucion/nuevoconsiderando.html', {'form': form})


def editarconsiderando(request):
    if request.method == "POST":
        form = ConsiderandoForm(request.POST)
        post_idcon = request.POST.get('idcon', False)
        if post_idcon is not None:
            try:
                con = Considerando.objects.get(id_considerando=post_idcon)
            except Considerando.DoesNotExist:
                con = None
    else:
        form = ConsiderandoForm

    return render(request, 'resolucion/editarconsiderando.html', {'form': form, 'con': con},)

def considerandoedit(request):
    if request.method == "POST":
        post_idcon = request.POST.get('idcon', False)
        con = Considerando.objects.get(id_considerando=post_idcon)
        con.resolucion_considerando = Resolucion.objects.get(nro_resolucion=request.POST.get('resolucion_considerando',False))
        con.nro_considerando = request.POST.get('nro_considerando',False)
        con.descripcion_considerando = request.POST.get('descripcion_considerando',False)
        con.save()
        return redirect('tablaresolucion')

    return render(request, 'resolucion/editarconsiderando.html',)

def eliminarconsiderando(request):
    if request.method == "POST":
        post_idcon = request.POST['idcon']
        if post_idcon is not None:
                try:
                    cons = Considerando.objects.get(id_considerando=post_idcon)
                    cons.delete()
                except Considerando.DoesNotExist:
                    cons = None
        return redirect('tablaresolucion')
    else:
        return redirect('tablaresolucion')

#resolutivo
def tablaresolutivo(request):
    resolutivos = Resolutivo.objects.all()
    return render(request, 'resolucion/tablaresolutivo.html',
                  {'resolutivos': resolutivos})


def nuevoresolutivo(request):
    if request.method == "POST":
        form = ResolutivoForm(request.POST)
        if form.is_valid():
            resolutivo = form.save(commit=False)
            resolutivo.save()
            return redirect('tablaresolucion')
    else:
        form = ResolutivoForm

    return render(request, 'resolucion/nuevoresolutivo.html', {'form': form})


def editarresolutivo(request):
    if request.method == "POST":
        form = ResolutivoForm(request.POST)
        post_idrst = request.POST.get('idrst', False)
        if post_idrst is not None:
            try:
                rst = Resolutivo.objects.get(id_resolutivo=post_idrst)
            except Resolutivo.DoesNotExist:
                rst = None
    else:
        form = ResolutivoForm
    return render(request,'resolucion/editarresolutivo.html', {'form':form, 'rst':rst})

def resolutivoedit(request):
    if request.method == "POST":
        post_idrst = request.POST.get('idrst', False)
        rst = Resolutivo.objects.get(id_resolutivo=post_idrst)
        rst.resolucion_resolutivo = Resolucion.objects.get(nro_resolucion=request.POST.get('resolucion_resolutivo',False))
        rst.nro_resolutivo = request.POST.get('nro_resolutivo',False)
        rst.descripcion_resolutivo = request.POST.get('descripcion_resolutivo',False)
        rst.save()
        return redirect('tablaresolucion')

    return render(request, 'resolucion/editarresolutivo.html',)

def eliminarresolutivo(request):
    if request.method == "POST":
        post_idrst = request.POST['idrst']
        if post_idrst is not None:
                try:
                    rst = Resolutivo.objects.get(id_resolutivo=post_idrst)
                    rst.delete()
                except Resolutivo.DoesNotExist:
                    rst = None
        return redirect('tablaresolucion')
    else:
        return redirect('tablaresolucion')


'expediente'
def tablaexpediente(request):
    expedientes = Expediente.objects.all()
    return render(request, 'resolucion/tablaexpediente.html',
                  {'expedientes': expedientes})


def nuevoexpediente(request):
    if request.method == "POST":
        form = ExpedienteForm(request.POST)
        if form.is_valid():
            expediente = form.save(commit=False)
            expediente.save()
            return redirect('tablaresolucion')
    else:
        form = ExpedienteForm

    return render(request, 'resolucion/nuevoexpediente.html', {'form': form})


def editarexpediente(request):
    if request.method == "POST":
        form = ExpedienteForm(request.POST)
        post_idexp = request.POST.get('idexp', False)
        if post_idexp is not None:
            try:
                exp = Expediente.objects.get(nro_expediente=post_idexp)
                exp.fecha_expediente = exp.fecha_expediente.strftime("%Y-%m-%d")
            except Expediente.DoesNotExist:
                exp = None
    else:
        form = ExpedienteForm
    return render(request, 'resolucion/editarexpediente.html', {'form': form, 'exp': exp})


def expedienteedit(request):
    if request.method == "POST":
        post_idexp = request.POST.get('idexp', False)
        exp = Expediente.objects.get(nro_expediente=post_idexp)
        exp.nro_expediente = request.POST.get('nro_expediente',False)
        exp.resolucion_expediente = Resolucion.objects.get(nro_resolucion=request.POST.get('resolucion_expediente',False))
        exp.fecha_expediente = request.POST.get('fecha_expediente',False)
        exp.facultad_expediente = Facultad.objects.get(id_facultad=request.POST.get('facultad_expediente',False))
        exp.dependencia_expediente = Dependencia.objects.get(id_dependencia=request.POST.get('dependencia_expediente',False))
        exp.descripcion_expediente = request.POST.get('descripcion_expediente',False)
        exp.save()
        return redirect('tablaresolucion')

    return render(request, 'resolucion/editarexpediente.html',)

def eliminarexpediente(request):
    if request.method == "POST":
        post_idexp = request.POST['idexp']
        if post_idexp is not None:
                try:
                    exp = Expediente.objects.get(nro_expediente=post_idexp)
                    exp.delete()
                except Expediente.DoesNotExist:
                    exp = None
        return redirect('tablaresolucion')
    else:
        return redirect('tablaresolucion')


'dependencia'
def tabladependencia(request):
    dependencias = Dependencia.objects.all()
    return render(request, 'resolucion/tabladependencia.html',
                  {'dependencias': dependencias})


def nuevodependencia(request):
    if request.method == "POST":
        form = DependenciaForm(request.POST)
        if form.is_valid():
            dependencia = form.save(commit=False)
            dependencia.save()
            return redirect('tablaresolucion')
    else:
        form = DependenciaForm

    return render(request, 'resolucion/nuevodependencia.html', {'form': form})


def editardependencia(request):
    if request.method == "POST":
        form = DependenciaForm(request.POST)
        post_iddep = request.POST.get('iddep', False)
        if post_iddep is not None:
            try:
                dep = Dependencia.objects.get(id_dependencia=post_iddep)
            except Dependencia.DoesNotExist:
                dep = None
    else:
        form = DependenciaForm
    return render(request, 'resolucion/editardependencia.html', {'form': form, 'dep': dep})

def dependenciaedit(request):
    if request.method == "POST":
        post_iddep = request.POST.get('iddep', False)
        dep = Dependencia.objects.get(id_dependencia=post_iddep)
        dep.id_dependencia = request.POST.get('id_depedencia',False)
        dep.facultad_dependencia = Facultad.objects.get(id_facultad=request.POST.get('facultad_expediente',False))
        dep.nombre_dependencia = request.POST.get('nombre_dependencia',False)
        dep.abreviatura_dependencia = request.POST.get('abreviatura_dependencia',False)
        dep.save()
        return redirect('tablaresolucion')

    return render(request, 'resolucion/editardependencia.html', )


def eliminardependencia(request):
    if request.method == "POST":
        post_iddep = request.POST['iddep']
        if post_iddep is not None:
            try:
                dep = Dependencia.objects.get(id_dependencia=post_iddep)
                dep.delete()
            except Dependencia.DoesNotExist:
                dep = None
        return redirect('tablaresolucion')
    else:
        return redirect('tablaresolucion')


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
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect('tablaresolucion')
    else:
        form = PersonaForm

    return render(request, 'resolucion/nuevopersona.html', {'form': form})


def editarpersona(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        post_idper = request.POST.get('idper', False)
        if post_idper is not None:
            try:
                per = Persona.objects.get(dni=post_idper)
            except Persona.DoesNotExist:
                per = None
    else:
        form = PersonaForm
    return render(request, 'resolucion/editarpersona.html', {'form': form, 'per': per})

def personaedit(request):
    if request.method == "POST":
        post_idper = request.POST.get('idper', False)
        per = Persona.objects.get(dni=post_idper)
        per.dni = request.POST.get('dni',False)
        per.nombre_persona = request.POST.get('nombre_persona',False)
        per.apellidos_persona = request.POST.get('apellidos_persona',False)
        per.tipo_persona = request.POST.get('tipo_persona',False)
        per.resoluciones = request.POST.get('resoluciones',False)
        per.save()
        return redirect('tablaresolucion')

    return render(request, 'resolucion/editarresolutivo.html',)

def eliminarpersona(request):
    if request.method == "POST":
        post_idper = request.POST['idper']
        if post_idper is not None:
                try:
                    per = Persona.objects.get(dni=post_idper)
                    per.delete()
                except Persona.DoesNotExist:
                    per = None
        return redirect('tablaresolucion')
    else:
        return redirect('tablaresolucion')

