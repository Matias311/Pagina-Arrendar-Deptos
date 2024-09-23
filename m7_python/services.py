from m7_python.models import Detalle_Usuario, Region, Comuna, Inmueble, Status
from django.contrib.auth.models import User


def crear_inmueble(data: dict, tipo_inmueble: Inmueble.Tipo_Inmueble) -> Inmueble:  # Crear Inmueble
    """
        data = {
            'id_inmueble': str,
            'id_user': int,
            'comuna_cod': str,
            'nombre': str,
            'descripcion': str,
            'm2_totales': int,
            'm2_construidos': int,
            'num_baños': int,
            'num_habitaciones': int,
            'num_estacionamientos': int,
            'direccion': str,
            'precio': int,
            'precio_ufs': float
        }
    """
    try:
        arrendador = User.objects.get(id=data['id_user'])
        comuna = Comuna.objects.get(id_comuna=data['comuna_cod'])
        inmueble = Inmueble(
            id_inmueble=data['id_inmueble'],
            nombre=data['nombre'],
            descripcion=data['descripcion'],
            m2_construidos=data['m2_construidos'],
            m2_terreno=data['m2_totales'],
            cant_estacionamiento=data['num_estacionamiento'],
            cant_banos=data['num_baños'],
            cant_habitaciones=data['num_habitaciones'],
            direccion=data['direccion'],
            tipo_inmueble=tipo_inmueble,
            precio_arriendo=data['precio'],
            arrendador=arrendador,
            comuna=comuna
        )
        inmueble.save()
        return inmueble
    except Exception as e:
        print(e)


def crear_region(id_region: str, nombre: str) -> Region:  # Crear Region
    try:
        region = Region(id_region=id_region, nombre=nombre)
        region.save()
        return region

    except Exception as e:
        print(e)


def crear_comuna(id_comuna: str, nombre: str, region: Region) -> Comuna:  # Crear Comuna
    try:
        comuna = Comuna(id_comuna=id_comuna, nombre=nombre, region=region)
        comuna.save()
        return comuna
    except Exception as e:
        print(e)


def crear_user(username: str, first_name: str, last_name: str, email: str) -> User:  # Crear User
    try:
        usuario = User(username=username, first_name=first_name,
                       last_name=last_name, email=email)
        usuario.save()
        return usuario
    except Exception as e:
        print(e)


def obtener_todos_inmuebles() -> list[Inmueble]:  # obtener_todos_los_inmuebles
    try:
        inmuebles = list(Inmueble.objects.all())
        return inmuebles
    except Exception as e:
        print(e)


# actualizar_descripcion_inmueble / update
def actualizar_descripcion_inmueble(id_inmueble: str, descripcion: str) -> Inmueble:
    try:
        inmueble = Inmueble.objects.get(id_idmueble=id_inmueble)
        inmueble.descripcion = descripcion
        inmueble.save()
        return inmueble
    except Exception as e:
        print(e)


# Actualizar disponibilidad
def actualizar_disponibilidad(id_inmueble: str, disponibilidad: bool) -> Inmueble:
    try:
        inmueble = Inmueble.objects.get(id_inmueble=id_inmueble)
        inmueble.disponible = disponibilidad
        inmueble.save()
        return inmueble
    except Exception as e:
        print(e)


# eliminar_inmueble - baneo (softDelete) -> is_active
def eliminar_inmueble(id_inmueble: str) -> Inmueble:
    try:
        inmueble = Inmueble.objects.get(id_inmueble=id_inmueble)
        inmueble.is_active = False
        inmueble.save()
        return inmueble
    except Exception as e:
        print(e)


# Elimina de la base de datos un inmueble
def eliminar_inmueble_db(id_inmueble: str) -> dict:
    try:
        inmueble = Inmueble.objects.get(id_inmueble=id_inmueble)
        inmueble.delete()
        return {
            "Tipo": "Exito",
            "Mensaje": "Se ha eliminado correctamente"
        }
    except Exception as e:
        print(e)


# Buscar usuario
def encontrar_crear_usuario(user) -> None:
    try:
        user_profile, created = Detalle_Usuario.objects.get_or_create(
            usuario=user)
        if created:
            print("Se creo un nuevo perfil del usuario")
        else:
            print("El perfil ya existia")
        return user_profile
    except Exception as e:
        print(e)
        return None
