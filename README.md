# Proyecto de APP INMUEBLE creado con Django

Este proyecto es una aplicación web desarrollada con el framework Django. Fue creado para probar mis conocimientos y está basado en una página de arriendo de inmuebles. La aplicación tiene dos vistas principales: una para arrendatarios y otra para arrendadores.

## Tecnologías Utilizadas
- **Django**: Framework web de alto nivel que promueve el desarrollo rápido y limpio.
- **PostgreSQL**: Sistema de gestión de bases de datos relacional utilizado para almacenar los datos.
- **Bootstrap**: Framework CSS para un diseño receptivo y móvil.
- **JavaScript**: Lenguaje de programación utilizado para la interactividad en el frontend.

## Funcionalidades:
- **Autenticación de usuarios**: Los usuarios pueden registrarse, iniciar sesión, editar su perfil y cerrar sesión.
- **Gestión de base de datos con ORM de Django**: Utiliza el ORM de Django para interactuar con una base de datos PostgreSQL.
- **Administración de contenido**: A través del panel de administración de Django, los administradores pueden gestionar usuarios, propiedades y solicitudes.
- **Rutas y vistas personalizables**: La aplicación incluye rutas y vistas para diferentes roles de usuarios (arrendatarios y arrendadores).
- **Plantillas HTML dinámicas**: Utiliza el sistema de plantillas de Django para generar contenido dinámico.
- **Base de datos POSTGRESQL**: Almacena los datos de la aplicación en una base de datos PostgreSQL.

## Flujo de usuarios:

### Arrendatario:
1. **Registro/Iniciar sesión**: El arrendatario se registra o inicia sesión en la aplicación.
2. **Buscar propiedades**: Puede buscar propiedades disponibles para arrendar.
3. **Ver detalles de la propiedad**: Puede ver los detalles de una propiedad específica.
4. **Solicitar inmueble**: Puede solicitar el arriendo de una propiedad.
5. **Ver solicitudes**: Puede gestionar el estado de sus solicitudes de arriendo.

### Arrendador:
1. **Registro/Iniciar sesión**: El arrendador se registra o inicia sesión en la aplicación.
2. **Publicar propiedades**: Puede agregar nuevas propiedades para arrendar.
3. **Gestionar propiedades**: Puede editar, eliminar propiedades y ver las solicitudes asociadas a estas.
4. **Cambiar estado de solicitudes**: Puede cambiar el estado de una solicitud de arriendo (Pendiente, Aprobada, Rechazada).

## URLs de la aplicación:
- **Home**: `http://127.0.0.1:8000/`
- **Registro de usuario**: `http://127.0.0.1:8000/accounts/register`
- **Seleccionar tipo de usuario**: `http://127.0.0.1:8000/registration/tipo_usuario`
- **Perfil de usuario**: `http://127.0.0.1:8000/accounts/perfil`
- **Editar perfil**: `http://127.0.0.1:8000/accounts/edit_perfil`
- **Sobre nosotros**: `http://127.0.0.1:8000/sobre_nosotros`
- **Contacto**: `http://127.0.0.1:8000/contacto`
- **Dashboard del arrendador**: `http://127.0.0.1:8000/arrendador/dashboard`
- **Home del arrendatario**: `http://127.0.0.1:8000/arrendatarior/home`
- **Crear inmueble**: `http://127.0.0.1:8000/arrendador/crear_inmueble`
- **Pre-eliminar inmueble**: `http://127.0.0.1:8000/arrendador/pre_eliminar_inmueble/<id_inmueble>`
- **Eliminar inmueble**: `http://127.0.0.1:8000/arrendador/pre_eliminar_inmueble/eliminar_inmueble/<id_inmueble>`
- **Editar inmueble**: `http://127.0.0.1:8000/arrendador/editar_inmueble/<id_inmueble>`
- **Ver estado de solicitudes**: `http://127.0.0.1:8000/arrendador/detalle_status/<id_inmueble>`
- **Cambiar estado de solicitud**: `http://127.0.0.1:8000/solicitud/cambiar_estado/<solicitud_id>`
- **Ver detalles de inmueble (arrendatario)**: `http://127.0.0.1:8000/arrendatario/detalle_inmueble/<id_inmueble>`
- **Solicitar inmueble**: `http://127.0.0.1:8000/arrendatario/peticion/<id_inmueble>`
- **Ver solicitudes del arrendatario**: `http://127.0.0.1:8000/arrendatario/solicitudes`
- **Página de error**: `http://127.0.0.1:8000/error`

## Características:
- Autenticación de usuarios
- Gestión de base de datos con ORM de Django
- Administración de contenido a través del panel de administración de Django
- Rutas y vistas personalizables
- Plantillas HTML dinámicas
- Base de datos POSTGRESQL

## Requisitos:
- Python 3.x
- Django 3.x o superior
- Base de datos (POSTGRESQL)

## Instalación:
1. Clonar el repositorio del proyecto:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    ```
2. Navegar al directorio del proyecto:
    ```sh
    cd <NOMBRE_DEL_PROYECTO>
    ```
3. Crear y activar un entorno virtual:
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usar `env\Scripts\activate`
    ```
4. Instalar las dependencias del proyecto:
    ```sh
    pip install -r requirements.txt
    ```
5. Crear archivo .env con la configuración de POSTGRESQL:
    ```env
    POSTGRES_DB=nombre_de_tu_base_de_datos
    POSTGRES_USER=tu_usuario
    POSTGRES_PASSWORD=tu_contraseña
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ```
6. Realizar las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```
7. Cargar datos a la base de datos:
   ```sh
    python manage.py loaddata m7_python/data/users.json
    python manage.py loaddata m7_python/data/regiones_comunas.json
    python manage.py loaddata m7_python/data/inmuebles.json
   ```

8. Iniciar el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Errores Comunes y Soluciones
- **Error de conexión a PostgreSQL**: Asegúrate de que PostgreSQL esté instalado y en ejecución, y verifica que la configuración en el archivo `.env` sea correcta.
- **Error al cargar datos**: Si no se encuentran archivos JSON al intentar cargar datos, verifica que la ruta especificada en los comandos sea correcta.

m7_python/
├── data/
│   ├── inmuebles.json
│   ├── regiones_comunas.json
│   └── users.json
├── migrations/
├── output/
│   └── outputs.txt
├── static/
│   └── js/
│       └── main.js
├── templates/
│   ├── arrendador/
│   │   ├── crear_inmueble.html
│   │   ├── dashboard.html
│   │   ├── detalle_inmueble.html
│   │   ├── editar_inmueble.html
│   │   └── eliminar_inmueble.html
│   ├── arrendatario/
│   │   ├── detalle_inmueble_usuario.html
│   │   ├── home.html
│   │   └── solicitudes.html
│   ├── registration/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── tipo_usuario.html
│   ├── base.html
│   ├── contacto.html
│   ├── editar_perfil.html
│   ├── error.html
│   ├── footer.html
│   ├── navbar.html
│   ├── perfil.html
│   └── sobre_nosotros.html
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── services.py
├── temp.py
├── tests.py
├── urls.py
└── views.py
