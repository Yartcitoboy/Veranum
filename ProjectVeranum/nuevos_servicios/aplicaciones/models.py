from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    ocupacion = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    
    def clean(self):
        # Validar que el RUT no exista previamente
        if Contacto.objects.filter(rut=self.rut).exclude(pk=self.pk).exists():
            raise ValidationError(f"El RUT {self.rut} ya está registrado.")

    def save(self, *args, **kwargs):
        # Llamar a la validación personalizada antes de guardar
        self.clean()
        super().save(*args, **kwargs)


class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=50)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.DurationField()
    requisitos = models.TextField()
    disponibilidad = models.BooleanField(default=True)
