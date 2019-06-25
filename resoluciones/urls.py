from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),

    path('resolucion/tabla', tablaresolucion, name='tablaresolucion'),
    path('resolucion/nuevo', nuevoresolucion, name='nuevoresolucion'),
    path('resolucion/editar', editarresolucion, name='editarresolucion'),
    path('resolucion/eliminar', eliminarresolucion, name='eliminarresolucion'),
    path('resolucion/edit', resolucionedit, name='resolucionedit'),


    path('considerando/tabla', tablaconsiderando, name='tablaconsiderando'),
    path('considerando/nuevo', nuevoconsiderando, name='nuevoconsiderando'),
    path('considerando/editar', editarconsiderando, name='editarconsiderando'),

    path('resolutivo/tabla', tablaresolutivo, name='tablaresolutivo'),
    path('resolutivo/nuevo', nuevoresolutivo, name='nuevoresolutivo'),
    path('resolutivo/editar', editarresolutivo, name='editarresolutivo'),

    path('dependencia/tabla', tabladependencia, name='tabladependencia'),
    path('dependencia/nuevo', nuevodependencia, name='nuevodependencia'),
    path('dependencia/editar', editardependencia, name='editardependencia'),

    path('expediente/tabla', tablaexpediente, name='tablaexpediente'),
    path('expediente/nuevo', nuevoexpediente, name='nuevoexpediente'),
    path('expediente/editar', editarexpediente, name='editarexpediente'),

    path('facultad/tabla', tablafacultad, name='tablafacultad'),

    path('persona/tabla', tablapersona, name='tablapersona'),
    path('persona/nuevo', nuevopersona, name='nuevopersona'),
    path('persona/editar', editarpersona, name='editarpersona'),
]