from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Detalle_Usuario(models.Model):
    # ENUMS para los tipos de usuarios
    class Tipo_Usuario(models.TextChoices):
        ARRENDADOR = 'Arrendador', 'Arrendador'
        ARRENDATARIO = 'Arrendatario', 'Arrendatario'

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, null=False, blank=False)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    tipo_usuario = models.CharField(
        choices=Tipo_Usuario.choices, default=Tipo_Usuario.ARRENDADOR)


class Comuna(models.Model):
    id_comuna = models.IntegerField()
    nombre = models.CharField(max_length=50, null=False, blank=False)


class Region(models.Model):
    id_region = models.IntegerField()
    nombre = models.CharField(max_length=50, null=False, blank=False)


class Inmueble(models.Model):
    # ENUMS para los tipos de inmuebles
    class Tipo_Inmueble(models.TextChoices):
        CASA = 'C', 'Casa'
        DEPARTAMENTO = 'D', 'Departamento'
        PARCELA = 'P', 'Parcela'

    id_inmueble = models.CharField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False, blank=False)
    descripcion = models.TextField(max_length=200, null=False, blank=False)
    disponible = models.BooleanField(default=True)
    m2_construidos = models.IntegerField()
    m2_terreno = models.IntegerField()
    cant_estacionamiento = models.IntegerField()
    cant_banos = models.IntegerField()
    cant_habitaciones = models.IntegerField()
    direccion = models.CharField(max_length=50, null=False, blank=False)
    tipo_inmueble = models.CharField(
        choices=Tipo_Inmueble.choices, default=Tipo_Inmueble.DEPARTAMENTO)
    precio_arriendo = models.IntegerField(null=False, blank=False)
    arrendador = models.ForeignKey(
        User, related_name='inmueble', on_delete=models.RESTRICT)  # Arrendador
    comuna = models.ForeignKey(
        Comuna, related_name='inmueble', on_delete=models.RESTRICT)
    region = models.ForeignKey(
        Region, related_name='inmueble', on_delete=models.CASCADE)


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
