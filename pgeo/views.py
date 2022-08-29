from django.shortcuts import render, get_object_or_404

from .models import *
# Create your views here.
def home(request):
    destinos = Rutas.objects.all()
    lugares = Empresa.objects.all()
    return render(request, 'home.html', {'destinos': destinos, 'lugares': lugares})