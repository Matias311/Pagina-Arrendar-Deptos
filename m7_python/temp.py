import os
import sys
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from django.contrib.auth.models import User
from m7_python.models import Inmueble

# Consultar listado de inmuebles para arriendo separado por comunas, solo usando los
# campos "nombre" y "descripción"
def listar_inmuebles_para_arriendo_comunas_raw(filtro: str):
    query ="""SELECT i.id_inmueble, i.nombre, i.descripcion FROM m7_python_inmueble i 
    JOIN m7_python_comuna c ON c.cod=i.comuna_id WHERE c.nombre ILIKE %s"""
    inmuebles = Inmueble.objects.raw(query, [f'{filtro}%'])

    with open("m7_python/output/outputs.txt", "a", encoding='UTF-8') as file:
        for i in inmuebles:
            file.write('Inmuebles en arriendo filtrando la comuna con raw\n'
                    f'{i.nombre} \n Descripcion: {i.descripcion}\n'
                    '---------------------------------------------\n')


def listar_inmuebles_para_arriendo_comunas_orm(filtro: str):
    inmuebles = Inmueble.objects.filter(comuna__nombre__icontains=filtro)

    with open("m7_python/output/outputs.txt", "a", encoding='UTF-8') as file:
        for i in inmuebles:
            file.write('Inmuebles en arriendo filtrando la comuna con orm\n'
                        f'{i.nombre} \n Descripcion: {i.descripcion}\n'
                       '---------------------------------------------\n') 
    


# Consultar listado de inmuebles para arriendo separado por regiones en un script
def listar_inmuebles_arriendo_regiones_raw(filtro: str):
    query = """
        SELECT i.id_inmueble, i.nombre AS inmueble_nombre, i.descripcion, i.precio_arriendo,
               c.nombre AS comuna_nombre, r.nombre AS region_nombre
        FROM m7_python_inmueble i
        JOIN m7_python_comuna c ON c.cod = i.comuna_id
        JOIN m7_python_region r ON c.region_id = r.cod WHERE r.nombre ILIKE %s
    """
    inmuebles = Inmueble.objects.raw(query, [f'%{filtro}%'])

    with open("m7_python/output/outputs.txt", "a", encoding='UTF-8') as file: 
        for i in inmuebles:
            file.write('Inmuebles en arriendo filtrando la region con raw\n'
                f'Inmueble: {i.inmueble_nombre}\nDescripción: {i.descripcion}\nPrecio: {i.precio_arriendo}\n'
                f'Comuna: {i.comuna_nombre}\nRegión: {i.region_nombre}\n'
                f'-------------------------------------------------------\n')


def listar_inmuebles_arriendo_regiones_orm(filtro: str):
    inmuebles = Inmueble.objects.filter(comuna__region__nombre__icontains=filtro)
    with open("m7_python/output/outputs.txt", "a", encoding='UTF-8') as file: 
        for i in inmuebles:
            file.write('Inmuebles en arriendo filtrando la region con orm\n'
                f'Inmueble: {i.nombre}\nDescripcion: {i.descripcion}\nPrecio: {i.precio_arriendo}\n'
                f'Comuna: {i.comuna.nombre}\nRegion: {i.comuna.region.nombre}\n'
                '----------------------------------------------------------\n')


def main():
    listar_inmuebles_para_arriendo_comunas_raw('i')
    listar_inmuebles_para_arriendo_comunas_orm('ta')
    listar_inmuebles_arriendo_regiones_raw("ta")
    listar_inmuebles_arriendo_regiones_orm("ta")

if __name__ == '__main__':
    main()
