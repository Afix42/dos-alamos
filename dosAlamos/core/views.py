from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/home.html')

def servicios(request):
    return render(request, 'core/service.html')

def registrarse(request):
    return render(request, 'core/registrarse.html')

def doctores(request):
    return render(request, 'core/doctores.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def clinica(request):
    return render(request, 'core/clinict.html')

def sesion(request):
    return render(request, 'core/sesion.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def citas(request):
    return render(request, 'core/citas.html')

def pacientes(request):
    return render(request, 'core/pacientes.html')

def ficha(request):
    return render(request, 'core/ficha.html')

