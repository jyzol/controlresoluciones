# Generated by Django 2.2.1 on 2019-06-04 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resoluciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultad',
            name='abreviatura_facultad',
            field=models.CharField(choices=[('fii', 'FII'), ('fiee', 'FIEE'), ('fisi', 'FISI')], max_length=6),
        ),
    ]
