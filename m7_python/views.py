import json
from django.shortcuts import render, redirect
from .services import obtener_todos_inmuebles, encontrar_crear_usuario, traer_inmuebles_arrendador, crear_inmuebles, eliminar_inmueble_db, traer_inmueble,  traer_estado_inmueble, crear_peticion_inmueble,  peticiones_usuario, traer_solicitudes_usuario
from .forms import RegisterForm, DetalleUserForm, UserEditForm, DetalleUserEditForm, ContactoForm, CrearInmuebleForm, InmuebleEditForm, FiltroComunaForm, FiltroRegionForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Status, Inmueble


# Define la vista home
@login_required
def home(req):
    if req.user.is_authenticated:
        detalle = encontrar_crear_usuario(req.user)
        if detalle.tipo_usuario == 'Arrendador':
            return redirect('dashboard')
        elif detalle.tipo_usuario == 'Arrendatario':
            return redirect('arrendatario_home')
        else:
            return redirect('login')
    else:
        return redirect('login')


# Vista arrendatario
@login_required
def arrendatario_home(req):
    inmuebles = Inmueble.objects.all()
    comuna_form = FiltroComunaForm(req.GET or None)
    region_form = FiltroRegionForm(req.GET or None)

    if comuna_form.is_valid():
        comuna = comuna_form.cleaned_data.get(
            'comuna')
        if comuna:
            inmuebles = inmuebles.filter(comuna=comuna)
            print("Filtrado por comuna:", inmuebles)
    else:
        inmuebles = obtener_todos_inmuebles()

    if region_form.is_valid():
        region = region_form.cleaned_data.get(
            'region')
        if region:
            inmuebles = inmuebles.filter(comuna__region=region)
            print("Filtrado por región:", inmuebles)
    else:
        inmuebles = obtener_todos_inmuebles()

    search_query = req.GET.get('search', '')
    if search_query:
        inmuebles = inmuebles.filter(nombre__icontains=search_query)

    return render(req, 'arrendatario/home.html', {
        'inmuebles': inmuebles,
        'region_form': region_form,
        'comuna_form': comuna_form
    })


# Vista arrendador:
@login_required
def arrendador_dashboard(req):
    usuario = req.user
    inmuebles = traer_inmuebles_arrendador(usuario)
    inactivos = inmuebles.filter(is_active=False).count()
    return render(req, 'arrendador/dashboard.html', {'inmuebles': inmuebles, 'inactivos': inactivos})


def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('tipo_usuario')
    else:
        form = RegisterForm()
    return render(req, 'registration/register.html', {'form': form})


@login_required
def tipoUsuario(req):
    user_profile = encontrar_crear_usuario(req.user)
    if req.method == 'POST':
        form = DetalleUserForm(req.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DetalleUserForm(instance=user_profile)
    return render(req, 'registration/tipo_usuario.html', {'form': form})


@login_required
def ver_perfil(req):
    user = req.user
    perfil = encontrar_crear_usuario(req.user)

    return render(req, 'perfil.html', {'user': user, 'perfil': perfil})


@login_required
def editar_perfil(req):
    user = req.user
    user_detalle = encontrar_crear_usuario(user)
    if req.method == 'POST':
        form_usuario = UserEditForm(req.POST, instance=user)
        form_detalle = DetalleUserEditForm(req.POST, instance=user_detalle)
        if form_usuario.is_valid() and form_detalle.is_valid():
            form_usuario.save()
            form_detalle.save()
            return redirect('perfil')
    else:
        form_usuario = UserEditForm(instance=user)
        form_detalle = DetalleUserEditForm(instance=user_detalle)
    return render(req, 'editar_perfil.html', {'form_usuario': form_usuario, 'form_detalle': form_detalle})


def sobre_nosotros(req):
    return render(req, 'sobre_nosotros.html', {})


def contacto(req):
    if req.method == 'POST':
        form = ContactoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactoForm()
    return render(req, 'contacto.html', {'form': form})


# Crear inmueble Arrendador
@login_required
def crear_inmueble(req):
    if req.method == 'POST':
        form = CrearInmuebleForm(req.POST)
        if form.is_valid():
            data = {
                'id_inmueble': form.cleaned_data['id_inmueble'],
                'nombre': form.cleaned_data['nombre'],
                'descripcion': form.cleaned_data['descripcion'],
                'disponible': form.cleaned_data['disponible'],
                'm2_construidos': form.cleaned_data['m2_construidos'],
                'm2_terreno': form.cleaned_data['m2_terreno'],
                'cant_estacionamiento': form.cleaned_data['cant_estacionamiento'],
                'cant_habitaciones': form.cleaned_data['cant_habitaciones'],
                'cant_banos': form.cleaned_data['cant_banos'],
                'direccion': form.cleaned_data['direccion'],
                'tipo_inmueble': form.cleaned_data['tipo_inmueble'],
                'precio_arriendo': form.cleaned_data['precio_arriendo'],
                'is_active': form.cleaned_data['is_active'],
                'comuna_cod': form.cleaned_data['comuna'].cod,
                'arrendador': req.user.id
            }
            print(form.cleaned_data['comuna'].nombre)
            crear_inmuebles(data)
            return redirect('dashboard')
    else:
        form = CrearInmuebleForm()
    return render(req, 'arrendador/crear_inmueble.html', {'form': form})


# eliminar un inmueble
@login_required
def pre_eliminar_inmueble(req, id_inmueble):
    inmueble = traer_inmueble(id_inmueble)
    return render(req, 'arrendador/eliminar_inmueble.html', {'inmueble': inmueble})


@login_required
def eliminar_inmueble(req, id_inmueble):
    eliminar_inmueble_db(id_inmueble)
    return redirect('dashboard')


# Editar inmueble
@login_required
def editar_inmueble(req, id_inmueble):
    inmueble = traer_inmueble(id_inmueble)
    if req.method == 'POST':
        form = InmuebleEditForm(req.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = InmuebleEditForm(instance=inmueble)
    return render(req, 'arrendador/editar_inmueble.html', {'form': form})


@login_required
def ver_lista_solicitudes(req, id_inmueble):
    inmueble = traer_inmueble(id_inmueble)
    # traer el status
    solicitudes = traer_estado_inmueble(id_inmueble)
    return render(req, 'arrendador/detalle_inmueble.html', {'inmueble': inmueble, 'solicitudes': solicitudes})


@csrf_exempt
def cambiar_estado_solicitud(request, solicitud_id):
    if request.method == 'POST':
        try:
            solicitud = Status.objects.get(id=solicitud_id)
            data = json.loads(request.body)
            nuevo_estado = data.get('estado')

            if nuevo_estado in [Status.Estado.PENDIENTE, Status.Estado.APROBADA, Status.Estado.RECHAZADA]:
                solicitud.estado = nuevo_estado
                solicitud.save()

                return JsonResponse({
                    'success': True,
                    'nuevo_estado': solicitud.get_estado_display()
                })
            else:
                return JsonResponse({'success': False, 'error': 'Estado no válido'})

        except Status.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Solicitud no encontrada'})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})


@login_required
def solicitar_inmueble(req, id_inmueble):
    usuario = req.user.id
    peticiones = peticiones_usuario(usuario, id_inmueble)
    if len(peticiones) == 0:
        status = crear_peticion_inmueble(id_inmueble, req.user.id)
        return redirect('home')
    else:
        return redirect('error')


@login_required
def detail_inmueble_user(req, id_inmueble):
    usuario = req.user.id
    inmueble = traer_inmueble(id_inmueble)
    peticiones = peticiones_usuario(usuario, id_inmueble)
    print(peticiones)
    return render(req, 'arrendatario/detalle_inmueble_usuario.html', {'inmueble': inmueble, 'peticiones': len(peticiones)})


def error_pagina(req):
    return render(req, 'error.html', {})


# Ver solicitudes
def ver_solicitudes(req):
    peticiones = traer_solicitudes_usuario(req.user.id)
    print(peticiones)
    return render(req, 'arrendatario/solicitudes.html', {'peticiones': peticiones})
