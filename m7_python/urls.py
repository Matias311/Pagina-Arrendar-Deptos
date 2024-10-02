from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register', views.register, name='register'),
    path('registration/tipo_usuario', views.tipoUsuario, name='tipo_usuario'),
    path('accounts/perfil', views.ver_perfil, name='perfil'),
    path('accounts/edit_perfil', views.editar_perfil, name='editar_perfil'),
    path('sobre_nosotros', views.sobre_nosotros, name='sobre_nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('arrendador/dashboard', views.arrendador_dashboard, name='dashboard'),
    path('arrendatarior/home', views.arrendatario_home, name='arrendatario_home'),
    path('arrendador/crear_inmueble', views.crear_inmueble, name='crear_inmueble'),
    path('arrendador/pre_eliminar_inmueble/<str:id_inmueble>/',
         views.pre_eliminar_inmueble, name='pre_eliminar_inmueble'),
    path('arrendador/pre_eliminar_inmueble/eliminar_inmueble/<str:id_inmueble>/',
         views.eliminar_inmueble, name='eliminar_inmueble'),
    path('arrendador/editar_inmueble/<str:id_inmueble>/',
         views.editar_inmueble, name='editar_inmueble'),
    path('arrendador/detalle_status/<str:id_inmueble>/',
         views.ver_lista_solicitudes, name='detalle_status'),
    path('solicitud/cambiar_estado/<int:solicitud_id>/',
         views.cambiar_estado_solicitud, name='cambiar_estado_solicitud'),

    path('arrendatario/detalle_inmueble/<str:id_inmueble>',
         views.detail_inmueble_user, name='detalle_inmueble_usuario'),
    path('arrendatario/peticion/<str:id_inmueble>/',
         views.solicitar_inmueble, name='peticion_inmueble'),
    path('error', views.error_pagina, name='error'),
    path('arrendatario/solicitudes', views.ver_solicitudes, name='solicitudes')
]
