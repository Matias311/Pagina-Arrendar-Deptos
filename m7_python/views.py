from django.shortcuts import render, redirect
from .services import obtener_todos_inmuebles, encontrar_crear_usuario, traer_inmuebles_arrendador
from .forms import RegisterForm, DetalleUserForm, UserEditForm, DetalleUserEditForm, ContactoForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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
    inmuebles = obtener_todos_inmuebles()
    return render(req, 'arrendatario/home.html', {'inmuebles': inmuebles})


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
