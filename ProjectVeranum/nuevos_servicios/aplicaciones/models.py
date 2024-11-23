from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=128)
    sexo = models.CharField(max_length=10)
    
    
    def clean(self):
        # Validar que el RUT no exista previamente
        if Usuario.objects.filter(rut=self.rut).exclude(pk=self.pk).exists():
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
