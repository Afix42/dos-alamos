from django.contrib import admin
from django.urls import path
from .views import home, servicios, registrarse, contacto, clinica,doctores,sesion,formulario, citas,pacientes,ficha, vista_medico, vista_paciente, vista_secretaria,registro_view,funcion_login,horas


urlpatterns = [
    path('', home, name='home'),
    path('servicios/',servicios,name="servicios"),
    path('registrarse/',registrarse,name="registrarse"),
    path('contacto/',contacto,name="contacto"),
    path('clinica/',clinica,name="clinica"),
    path('doctores/',doctores,name="doctores"),
    path('sesion/',sesion,name="sesion"),
    path('formulario/<id>/',formulario,name="formulario"),
    path('citas/',citas,name="citas"),
    path('pacientes/',pacientes,name="pacientes"),
    path('ficha/',ficha,name="ficha"),
    path('vista_paciente/',vista_paciente,name="vista_paciente"),
    path('vista_medico/',vista_medico,name="vista_medico"),
    path('vista_secretaria/',vista_secretaria,name="vista_secretaria"),
    path('registro_view',registro_view,name='registro_view'),
    path('funcion_login',funcion_login,name='funcion_login'),
    path('horas/',horas,name="horas"),
]