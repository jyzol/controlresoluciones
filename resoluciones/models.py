from django.db import models

# Create your models here.


class Facultad(models.Model):
    FACS = (
        ('fii', 'FII'),
        ('fiee','FIEE'),
        ('fisi','FISI')
    )
    id_facultad = models.CharField(max_length=3, primary_key=True)
    nombre_facultad = models.CharField(max_length=100)
    abreviatura_facultad = models.CharField(max_length=6, choices=FACS)

    def __str__(self):
        return self.abreviatura_facultad


class Dependencia(models.Model):
    id_dependencia = models.CharField(max_length=3, primary_key=True)
    facultad_dependencia = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    nombre_dependencia = models.CharField(max_length=50)
    abreviatura_dependencia = models.CharField(max_length=6)

    def __str__(self):
        return self.abreviatura_dependencia


class Resolucion(models.Model):
    nro_resolucion = models.CharField(max_length=5, primary_key=True)
    facultad_resolucion = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    # proviene_resolucion = models.ForeignKey(Resolucion, on_delete=models.CASCADE,null=True)
    fecha_resolucion = models.DateField()
    link_descarga = models.CharField(max_length=100)
    descripcion_resolucion = models.TextField
    anio_resolucion = models.CharField(max_length=4)
    estado_resolucion = models.CharField(max_length=20)
    observacion = models.TextField()
    adjunto = models.CharField(max_length=100)
    tipo_elevacion = models.CharField(max_length=50)

    class Meta:
        ordering = ('-fecha_resolucion',)

    def __str__(self):
        return self.nro_resolucion


class Resolutivo(models.Model):
    id_resolutivo = models.AutoField(primary_key=True)
    resolucion_resolutivo = models.ForeignKey(Resolucion, on_delete=models.CASCADE)
    nro_resolutivo = models.IntegerField()
    descripcion_resolutivo = models.TextField()

    def __str__(self):
        return self.nro_resolucion+" : "+self.nro_resolutivo


class Considerando(models.Model):
    id_considerando = models.AutoField(primary_key=True)
    resolucion_considerando = models.ForeignKey(Resolucion, on_delete=models.CASCADE)
    nro_considerando = models.IntegerField()
    descripcion_considerando = models.TextField()

    def __str__(self):
        return self.nro_resolucion+" : "+self.nro_resolutivo


class Persona(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    nombre_persona = models.CharField(max_length=100)
    apellidos_persona = models.CharField(max_length=100)
    tipo_persona = models.CharField(max_length=50)
    resoluciones = models.ManyToManyField(Resolucion)

    def __str__(self):
        return self.apellidos_persona+" "+self.nombre_persona


class Expediente(models.Model):
    nro_expediente = models.CharField(max_length=5, primary_key=True)
    resolucion_expediente = models.ForeignKey(Resolucion, on_delete=models.CASCADE)
    facultad_expediente = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    dependencia_expediente = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    descripcion_expediente = models.TextField()
    fecha_expediente = models.DateField()

    def __str__(self):
        return self.nro_expediente













