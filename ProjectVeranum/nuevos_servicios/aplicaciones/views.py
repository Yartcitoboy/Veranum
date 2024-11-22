from django.shortcuts import render, redirect
from .models import Comuna, Contacto, Servicio
# import cx_Oracle

def index(request):
    return render(request, 'web/index.html')

def form(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        rut = request.POST.get("run")
        telefono = request.POST.get("fono")
        direccion = request.POST.get("direccion")
        comuna = request.POST.get("comuna")
        profesion = request.POST.get("profesion")
        sexo = request.POST.get("sexo")
        ocupacion = request.POST.get("ocupacion")
        puesto = request.POST.get("puesto")

        comuna, created = Comuna.objects.get_or_create(nombre=comuna)

        contacto = Contacto.objects.create(
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

        return redirect('certificado')
    contacto = Contacto.objects.all() 

    return render(request, 'web/vistas/form.html', {'lista_contactos': contacto})

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
        if disponibilidad:
            services = services.filter(disponibilidad=True)

        results = services

    return render(request, 'web/vistas/servicios.html', {'results': results})




