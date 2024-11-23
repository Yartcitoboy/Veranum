from django.shortcuts import render, redirect
from .models import Usuario, Servicio 
from django.contrib import messages
from .form import LoginForm
from django.core.exceptions import ValidationError
# import cx_Oracle

def index(request):
    # Verificar si el usuario está logueado (si hay un usuario en la sesión)
    usuario_nombre = request.session.get('usuario_nombre', None)

    # Mostrar el mensaje de bienvenida si existe
    if messages.get_messages(request):
        return render(request, 'web/index.html', {'messages': messages.get_messages(request), 'usuario_nombre': usuario_nombre})

    return render(request, 'web/index.html', {'usuario_nombre': usuario_nombre})

def form(request):
    error_message = None  # Inicializamos error_message aquí

    if request.POST:
        # Obtener datos del formulario
        nombre = request.POST.get("nombre")
        rut = request.POST.get("run")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        sexo = request.POST.get("sexo")

        # Validar si el RUT ya está registrado
        if Usuario.objects.filter(rut=rut).exists():
            error_message = f"El RUT {rut} ya está registrado."
        else:
            
            usuario = Usuario(
                nombre=nombre,
                rut=rut,
                email=email,
                password=password,
                sexo=sexo,

            )

            try:
                usuario.full_clean()  # Validar el objeto
                usuario.save()  # Guardar en la base de datos
                return redirect('certificado')
            except ValidationError as e:
                # Capturar errores de validación
                error_message = str(e)

    # Siempre asignamos una lista de contactos para el caso GET o cualquier error
    lista_contactos = Usuario.objects.all()

    return render(request, 'web/vistas/form.html', {'lista_contactos': lista_contactos, 'error_message': error_message})

def login_view(request):
    if request.method == 'POST':
        rut = request.POST.get('run')
        password = request.POST.get('pass')

        # Validar RUT y contraseña en la base de datos
        usuario = Usuario.objects.filter(rut=rut).first()
        if usuario and usuario.password == password:
            # Almacenar información en la sesión
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nombre'] = usuario.nombre
            messages.success(request, f"¡Bienvenido {usuario.nombre}!")
            return redirect('/')  # Redirigir al index
        else:
            messages.error(request, "RUT o contraseña incorrectos.")
            return render(request, 'web/vistas/login.html', {
                'error': True
            })
    
    return render(request, 'web/vistas/login.html')

def mi_vista(request):
    # Código de la vista...
    return redirect(reverse('logout'))

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




