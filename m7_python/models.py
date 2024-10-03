from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import uuid
# Create your models here.


class Detalle_Usuario(models.Model):
    # ENUMS para los tipos de usuarios
    class Tipo_Usuario(models.TextChoices):
        ARRENDADOR = 'Arrendador', 'Arrendador'
        ARRENDATARIO = 'Arrendatario', 'Arrendatario'

    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='detalle_usuario')
    rut = models.CharField(max_length=9, null=False, blank=False, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9, null=True)
    tipo_usuario = models.CharField(
        choices=Tipo_Usuario.choices, default=Tipo_Usuario.ARRENDADOR, max_length=30)

    def __str__(self) -> str:
        return f'Nombre: {self.usuario.first_name} {self.usuario.last_name} Rut: {self.rut} Tipo de usuario: {self.tipo_usuario}'


class Region(models.Model):
    cod = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.nombre}'


class Comuna(models.Model):
    cod = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(
        Region, on_delete=models.RESTRICT, related_name='comunas')

    def __str__(self) -> str:
        return f'{self.nombre}'


class Inmueble(models.Model):
    # ENUMS para los tipos de inmuebles
    class Tipo_Inmueble(models.TextChoices):
        CASA = 'C', 'Casa'
        DEPARTAMENTO = 'D', 'Departamento'
        PARCELA = 'P', 'Parcela'

    id_inmueble = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=350, null=False, blank=False)
    descripcion = models.TextField(max_length=1200, null=False, blank=False)
    disponible = models.BooleanField(default=True)
    m2_construidos = models.IntegerField(
        validators=[MinValueValidator(1)], default=1)
    m2_terreno = models.IntegerField(
        validators=[MinValueValidator(1)], default=1)
    cant_estacionamiento = models.IntegerField(default=1)
    cant_habitaciones = models.IntegerField(
        validators=[MinValueValidator(1)], default=1)
    cant_banos = models.IntegerField(
        validators=[MinValueValidator(1)], default=1)
    direccion = models.CharField(max_length=150, null=False, blank=False)
    tipo_inmueble = models.CharField(
        choices=Tipo_Inmueble.choices, default=Tipo_Inmueble.DEPARTAMENTO)
    precio_arriendo = models.IntegerField(
        null=False, blank=False, validators=[MinValueValidator(1000)])
    is_active = models.BooleanField(default=True)
    comuna = models.ForeignKey(
        Comuna, related_name='inmuebles', on_delete=models.RESTRICT)
    arrendador = models.ForeignKey(
        User, related_name='inmuebles', on_delete=models.RESTRICT)  # Arrendador

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nDisponible:{self.disponible}\nTipo de inmueble: {self.tipo_inmueble}\nPrecio de arriendo: {self.precio_arriendo}'


class Status(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'P', 'Pendiente'
        RECHAZADA = 'R', 'Rechazada'
        APROBADA = 'A', 'Aprobada'

    estado = models.CharField(choices=Estado.choices, default=Estado.PENDIENTE)
    fecha = models.DateTimeField(auto_now_add=True)
    inmueble = models.ForeignKey(
        Inmueble, related_name='status', on_delete=models.RESTRICT)
    arrendatario = models.ForeignKey(
        User, related_name='status', on_delete=models.RESTRICT)  # Arrendatario

    def __str__(self) -> str:
        return f'Estado: {self.estado} Inmueble: {self.inmueble.nombre} Arrendatario: {self.arrendatario.first_name} {self.arrendatario.last_name}'


class Contacto(models.Model):
    id_contacto = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    mensaje = models.TextField(max_length=500, null=False, blank=False)
