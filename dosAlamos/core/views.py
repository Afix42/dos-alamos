from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/Home.html')

def Servicios(request):
    return render(request, 'core/service.html')

def Registro(request):
    return render(request, 'core/Registrarse.html')

def Doctores(request):
    return render(request, 'core/doctores.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def clinica(request):
    return render(request, 'core/clinict.html')
