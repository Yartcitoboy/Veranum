from django.shortcuts import render, redirect
from .models import Comuna, Contacto, Servicio
from django.core.exceptions import ValidationError
# import cx_Oracle

def index(request):
    return render(request, 'web/index.html')

def form(request):
    error_message = None  # Inicializamos error_message aquí
    contacto = None  # Inicializamos contacto en caso de error

    if request.POST:
        # Obtener datos del formulario
        nombre = request.POST.get("nombre")
        rut = request.POST.get("run")
        telefono = request.POST.get("fono")
        direccion = request.POST.get("direccion")
        comuna = request.POST.get("comuna")
        profesion = request.POST.get("profesion")
        sexo = request.POST.get("sexo")
        ocupacion = request.POST.get("ocupacion")
        puesto = request.POST.get("puesto")

        # Validar si el RUT ya está registrado
        if Contacto.objects.filter(rut=rut).exists():
            error_message = f"El RUT {rut} ya está registrado."
        else:
            comuna, created = Comuna.objects.get_or_create(nombre=comuna)

            contacto = Contacto(
                nombre=nombre,
                rut=rut,
                telefono=telefono,
                direccion=direccion,
                comuna=comuna,
                profesion=profesion,
                sexo=sexo,
                ocupacion=ocupacion,
                puesto=puesto
            )

            try:
                contacto.full_clean()  # Validar el objeto
                contacto.save()  # Guardar en la base de datos
                return redirect('certificado')
            except ValidationError as e:
                # Capturar errores de validación
                error_message = str(e)

    # Siempre asignamos una lista de contactos para el caso GET o cualquier error
    lista_contactos = Contacto.objects.all()

    return render(request, 'web/vistas/form.html', {'lista_contactos': lista_contactos, 'error_message': error_message, 'contacto': contacto})


def certificado(request):
    return render(request, 'web/certificado.html')

def servicio(request):
    results = []
    if request.GET:
        nombre_servicio = request.GET.get('nombre_servicio')
        descripcion = request.GET.get('descripcion')
        costo = request.GET.get('costo')
        duracion = request.GET.get('duracion')
        requisitos = request.GET.get('requisitos')
        disponibilidad = request.GET.get('disponibilidad')

        services = Servicio.objects.all()

        if nombre_servicio:
            services = services.filter(nombre_servicio__icontains=nombre_servicio)
        if descripcion:
            services = services.filter(descripcion__icontains=descripcion)
        if costo:
            services = services.filter(costo=costo)
        if duracion:
            services = services.filter(duracion=duracion)
        if requisitos:
            services = services.filter(requisitos__icontains=requisitos)
        if disponibilidad == 'true':
            services = services.filter(disponibilidad=True)

        results = services

    return render(request, 'web/vistas/servicios.html', {'results': results})




