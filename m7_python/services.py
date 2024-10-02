from m7_python.models import Detalle_Usuario, Region, Comuna, Inmueble, Status
from django.contrib.auth.models import User


def crear_inmuebles(data: dict) -> Inmueble:  # Crear Inmueble
    """
        data = {
            'id_inmueble': str,
            'nombre': str,
            'descripcion': str,
            'disponible': str,
            'm2_construidos': int,
            'm2_terreno': int,
            'cant_estacionamiento': int,
            'cant_habitaciones': int,
            'cant_banos': int,
            'direccion': str,
            'tipo_inmueble': str,
            'precio_arriendo': int,
            'is_active': bool,
            'comunacod': str,
            'arrendador': str,
        }
    """
    try:
        arrendador = User.objects.get(id=data['arrendador'])
        comuna = Comuna.objects.get(cod=data['comuna_cod'])

        inmueble = Inmueble(
            id_inmueble=data['id_inmueble'],
            nombre=data['nombre'],
            descripcion=data['descripcion'],
            disponible=data['disponible'],
            m2_construidos=data['m2_construidos'],
            m2_terreno=data['m2_terreno'],
            cant_estacionamiento=data['cant_estacionamiento'],
            cant_habitaciones=data['cant_habitaciones'],
            cant_banos=data['cant_banos'],
            direccion=data['direccion'],
            tipo_inmueble=data['tipo_inmueble'],
            precio_arriendo=data['precio_arriendo'],
            is_active=data['is_active'],
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


# Traer inmuebles de un arrendador
def traer_inmuebles_arrendador(arrendador: User) -> list[Inmueble]:
    try:
        tipo_usuario: str = arrendador.detalle_usuario.tipo_usuario
        if tipo_usuario != 'Arrendador':
            print('No es arrendador')
            return []
        inmuebles: list[Inmueble] = Inmueble.objects.filter(
            arrendador=arrendador)
        if not inmuebles.exists():
            print('No hay inmuebles')
            return []
        return inmuebles
    except Exception as e:
        print(e)


# Traer inmueble
def traer_inmueble(id_inmueble: str) -> Inmueble:
    try:
        inmueble = Inmueble.objects.get(id_inmueble=id_inmueble)
        return inmueble
    except Exception as e:
        print(e)


# Traer el estado del inmueble del arrendador
def traer_estado_inmueble(id_inmueble: str) -> list[Status]:
    try:
        status = Status.objects.filter(inmueble=id_inmueble)
        return status
    except Exception as e:
        print(e)


# Crear una peticion de inmueble
def crear_peticion_inmueble(id_inmueble: str, id_user: int) -> Status:
    try:
        inmueble = traer_inmueble(id_inmueble)
        usuario = User.objects.get(id=id_user)
        status_user = Status(inmueble=inmueble, arrendatario=usuario)
        status_user.save()
        return status_user
    except Exception as e:
        print(e)


# Traer las peticiones de cada usuario
def peticiones_usuario(id_usuario: int, id_inmueble: str) -> list[Status]:
    try:
        peticiones = Status.objects.filter(
            arrendatario__id=id_usuario, inmueble__id_inmueble=id_inmueble)
        return peticiones
    except Exception as e:
        print(e)


# Traer status de solicitudes de un inmueble
def traer_solicitudes_inmuble(id: int) -> list[Status]:
    try:
        stados = Status.objects.filter(id=id)
        return stados
    except Exception as e:
        print(e)


# Treaer todas las solicitudes de un usuario
def traer_solicitudes_usuario(id_usuario: int) -> list[Status]:
    try:
        stados = Status.objects.filter(arrendatario__id=id_usuario)
        return stados
    except Exception as e:
        print(e)
