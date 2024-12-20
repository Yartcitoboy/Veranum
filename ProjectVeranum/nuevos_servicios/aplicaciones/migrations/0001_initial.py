# Generated by Django 5.0.6 on 2024-07-01 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duracion', models.DurationField()),
                ('requisitos', models.TextField()),
                ('disponibilidad', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=100)),
                ('profesion', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('ocupacion', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicaciones.comuna')),
            ],
        ),
    ]
