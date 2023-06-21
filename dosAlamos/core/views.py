from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rol, Comuna, HoraTomada
from django.contrib.auth.decorators import login_required
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
    comuna = Comuna.objects.all
    medico = User.objects.filter(rol__nombreRol__icontains='Medico')

    data = {
        'usuario':usuario,
        'medico':medico,
        'comuna':comuna
    }


    return render(request, 'core/formulario.html', data)

def citas(request, id):
    usuario = get_object_or_404(User, pk=id)
    horas_abiertas = HoraTomada.objects.filter(estado='abierto')

    data = {
        'usuario':usuario,
        'horas_abiertas':horas_abiertas
    }
    return render(request, 'core/citas.html', data)

def pacientes(request):
    return render(request, 'core/pacientes.html')

def ficha(request):
    return render(request, 'core/ficha.html')

def vista_medico(request):
    return render(request, 'core/vista_medico.html')

@login_required
def vista_paciente(request):
    user_id = request.user.id  # Obtener el ID del usuario logueado
    context = {'user_id': user_id}
    return render(request, 'core/vista_paciente.html', context)

def vista_secretaria(request):
    user_id = request.user.id  # Obtener el ID del usuario logueado
    context = {'user_id': user_id}
    return render(request, 'core/vista_secretaria.html', context)

def horas(request):
    return render(request, 'core/horas.html')

@receiver(post_save, sender=User)
def set_default_rol(sender, instance, created, **kwargs):
    if created:
        Rol.objects.get_or_create(user=instance, nombreRol='Paciente')


def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        password = request.POST['password']
        repeat_password = request.POST['repeatPassword']
        email = request.POST['email']
        
        if password == repeat_password:
            try:
                user = User.objects.create_user(username=nombre, password=password)
                user.first_name = nombre
                user.last_name = apellido
                user.email = email
                user.save()

                # Asignar rol de "paciente" al nuevo usuario solo si no tiene ya asignado el rol
                rol_paciente, created = Rol.objects.get_or_create(user=user, nombreRol='Paciente')
                if not created:
                    # El rol "Paciente" ya existe para este usuario
                    messages.warning(request, 'El usuario ya tiene asignado el rol de Paciente.')

                # Verificar si el rol "médico" ya existe
                rol_medico, _ = Rol.objects.get_or_create(nombreRol='Medico')
                if rol_medico.user is None:
                    rol_medico.user = user
                    rol_medico.save()
                    # Asignar al usuario al grupo "médico" si existe
                    group_medico, _ = Group.objects.get_or_create(name='Medico')
                    user.groups.add(group_medico)

                user = authenticate(request, username=nombre, password=password)
                login(request, user)
                return redirect('login')
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

def guardar_hora(request):
    if request.method == 'POST':
        paciente = request.user
        medico_id = request.POST.get('medico')
        fecha = request.POST.get('Fecha')
        hora = request.POST.get('Hora')
        apellido_paciente = request.POST.get('apellidoPaciente')  # Modificación aquí
        nombre_comuna = request.POST.get('nombreComuna')  # Modificación aquí
        
        if medico_id and fecha and hora:
            try:
                medico = User.objects.get(id=medico_id)
                hora_tomada = HoraTomada(
                    nombrePaciente=paciente,
                    apellidoPaciente=apellido_paciente,
                    nombreComuna=nombre_comuna,
                    correoPaciente=paciente.email,  # Nuevo campo añadido
                    hora=hora,
                    doctor=medico,
                    estado='abierto'
                )
                hora_tomada.save()
                messages.success(request, 'La hora ha sido reservada exitosamente.')
                return redirect('vista_paciente')
            except User.DoesNotExist:
                messages.error(request, 'No se encontró el médico seleccionado.')
        else:
            messages.error(request, 'Debe completar todos los campos del formulario.')
    else:
        messages.error(request, 'El formulario debe ser enviado mediante el método POST.')
    
    return render(request, 'core/Formulario.html')


def eliminar_pacientes(request, id):
    horaT = HoraTomada.objects.get(pk = id)
    horaT.delete()
    secretaria = get_object_or_404(User, pk=27)  # Obtener el usuario secretaria con ID 27
    messages.success(request, 'Hora rechazada.')

    return redirect('citas', secretaria.pk)

def aceptar_hora(request, id):
    horaT = HoraTomada.objects.get(pk = id)
    horaT.estado = 'cerrado'
    horaT.save()
    secretaria = get_object_or_404(User, pk=27)  # Obtener el usuario secretaria con ID 27
    messages.success(request, 'Hora aprobada.')

    return redirect('citas', secretaria.pk)