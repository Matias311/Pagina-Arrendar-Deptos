from django.shortcuts import render
from .services import obtener_todos_inmuebles

# Define la vista home


def home(request):
    inmuebles = obtener_todos_inmuebles()
    return render(request, 'home.html', {'inmuebles': inmuebles})
