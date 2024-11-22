from django.contrib import admin
from .models import Contacto, Servicio, Comuna
# Register your models here.
admin.site.register(Comuna)
admin.site.register(Servicio)
admin.site.register(Contacto)