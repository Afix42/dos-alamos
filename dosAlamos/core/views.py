from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

def formulario(request, id):
    usuario = get_object_or_404(User, pk=id)
    medico = User.objects.filter(rol='14')

    data = {
        'usuario':usuario,
        'medico':medico
    }


    return render(request, 'core/formulario.html', data)

def citas(request):
    return render(request, 'core/citas.html')

def pacientes(request):
    return render(request, 'core/pacientes.html')

def ficha(request):
    return render(request, 'core/ficha.html')

def vista_medico(request):
    return render(request, 'core/vista_medico.html')

def vista_paciente(request):
    return render(request, 'core/vista_paciente.html')

def vista_secretaria(request):
    return render(request, 'core/vista_secretaria.html')

def horas(request):
    return render(request, 'core/horas.html')

def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        password = request.POST['password']
        repeat_password = request.POST['repeatPassword']
        email = request.POST['email']
        if password == repeat_password:
            try:
                # Crea un nuevo usuario utilizando la tabla User de Django
                user = User.objects.create_user(username=nombre, password=password)
                # Agrega los campos personalizados al usuario
                user.first_name = nombre
                user.last_name = apellido
                user.email = email
                user.save()
                # Inicia sesión automáticamente después del registro
                user = authenticate(request, username=nombre, password=password)
                login(request, user)
                return redirect('login')  # Redirige a la página de inicio después del registro exitoso
            except Exception as e:
                messages.error(request, f'Error al registrar el usuario: {str(e)}')
        else:
            messages.error(request, 'Las contraseñas no coinciden')

    return render(request, 'core/Registrarse.html')



def funcion_login(request):
    if request.method == 'POST':
        username = request.POST['nombre']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.rol.nombreRol == 'Medico':
                return redirect('vista_medico')  # Redirige al médico (administrador) a la vista de administrador
            elif user.rol.nombreRol == 'Secretaria':
                return redirect('vista_secretaria')  # Redirige a la secretaria a la vista de secretaria
            else:
                return redirect('vista_paciente')  # Redirige al paciente a la vista de paciente

        messages.error(request, 'El usuario y/o contraseña no coinciden o no existen.')
        return render(request, 'core/Sesion.html')

    return render(request, 'core/Sesion.html')

