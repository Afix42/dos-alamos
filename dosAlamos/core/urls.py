from django.contrib import admin
from django.urls import path
from .views import home, servicios, registrarse, contacto, clinica,doctores,sesion,formulario, citas,pacientes,ficha, vista_medico, vista_paciente,\
     vista_secretaria,registro_view,funcion_login,funcion_logout,horas,guardar_hora, eliminar_pacientes,aceptar_hora,mostrar_horas_tomadas, CrearFicha, MostrarFicha


urlpatterns = [
    path('', home, name='home'),
    path('servicios/', servicios, name="servicios"),
    path('registrarse/', registrarse, name="registrarse"),
    path('contacto/', contacto, name="contacto"),
    path('clinica/', clinica, name="clinica"),
    path('doctores/', doctores, name="doctores"),
    path('sesion/', sesion, name="sesion"),
    path('vista_paciente/formulario/<int:id>/', formulario, name="formulario"),
    path('vista_secretaria/citas/<id>/', citas, name="citas"),
    path('pacientes/<id>/', pacientes, name="pacientes"),
    path('ficha/', ficha, name="ficha"),
    path('vista_paciente/', vista_paciente, name="vista_paciente"),
    path('vista_medico/', vista_medico, name="vista_medico"),
    path('vista_secretaria/', vista_secretaria, name="vista_secretaria"),
    path('registro_view', registro_view, name='registro_view'),
    path('funcion_login', funcion_login, name='funcion_login'),
    path('funcion_logout', funcion_logout, name='funcion_logout'),
    path('horas/', horas, name="horas"),
    path('guardar_hora', guardar_hora, name="guardar_hora"),
    path('eliminar_pacientes/<id>/', eliminar_pacientes, name='eliminar_pacientes'),
    path('aceptar_hora/<id>/', aceptar_hora, name='aceptar_hora'),
    path('mostrar_horas_tomadas/<id>',mostrar_horas_tomadas, name='mostrar_horas_tomadas'),
    path('CrearFicha', CrearFicha, name="CrearFicha"),
    path('MostrarFicha/<hora_tomada_id>/', MostrarFicha, name='MostrarFicha'),
]