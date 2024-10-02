from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Detalle_Usuario, Contacto, Inmueble, Status, Comuna, Region

# Creación de formulario para crear usuario


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')


# Creacion de formulario para crear el detalle del usuario
class DetalleUserForm(forms.ModelForm):
    class Meta:
        model = Detalle_Usuario
        fields = ['rut', 'direccion', 'telefono', 'tipo_usuario']


# Edicion del usuario
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# Edicion del detalle usuario
class DetalleUserEditForm(forms.ModelForm):
    class Meta:
        model = Detalle_Usuario
        fields = ['rut', 'direccion', 'telefono']


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['email', 'nombre', 'apellido', 'mensaje']


# Crear inmueble
class CrearInmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['id_inmueble', 'nombre', 'descripcion', 'disponible',
                  'm2_construidos', 'm2_terreno', 'cant_estacionamiento', 'cant_habitaciones', 'cant_banos', 'direccion', 'tipo_inmueble', 'precio_arriendo', 'is_active', 'comuna']


# Editar inmueble
class InmuebleEditForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'disponible',
                  'm2_construidos', 'm2_terreno', 'cant_estacionamiento', 'cant_habitaciones', 'cant_banos', 'direccion', 'tipo_inmueble', 'precio_arriendo', 'is_active', 'comuna']


# Filtro de comuna
class FiltroComunaForm(forms.Form):
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        required=False,
        empty_label='Seleccione una Comuna',
        label='Comuna'
    )


# Filtro de region
class FiltroRegionForm(forms.Form):
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        empty_label='Seleccione una Region',
        label='Region'
    )
