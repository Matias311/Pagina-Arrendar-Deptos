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
    path('dashboard', views.arrendador_dashboard, name='dashboard'),
    path('arrendatario_home', views.arrendatario_home, name='arrendatario_home')
]
