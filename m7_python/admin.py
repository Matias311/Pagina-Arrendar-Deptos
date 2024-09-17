from django.contrib import admin
from .models import Detalle_Usuario, Comuna, Region, Inmueble, Status

# Register your models here.
admin.site.register(Detalle_Usuario)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Inmueble)
admin.site.register(Status)
