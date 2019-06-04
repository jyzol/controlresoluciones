# Generated by Django 2.2.1 on 2019-06-04 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resoluciones', '0002_auto_20190603_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resolucion',
            old_name='adjunto',
            new_name='adjunto_resolucion',
        ),
        migrations.RenameField(
            model_name='resolucion',
            old_name='observacion',
            new_name='observacion_resolucion',
        ),
        migrations.RemoveField(
            model_name='resolucion',
            name='anio_resolucion',
        ),
        migrations.AddField(
            model_name='resolucion',
            name='descripcion_resolucion',
            field=models.TextField(default='obs'),
        ),
    ]