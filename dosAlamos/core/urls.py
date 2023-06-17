from django.contrib import admin
from django.urls import path
from .views import home, servicios, registrarse, contacto, clinica,doctores,sesion,formulario, citas


urlpatterns = [
    path('', home, name='home'),
    path('servicios/',servicios,name="servicios"),
    path('registrarse/',registrarse,name="registrarse"),
    path('contacto/',contacto,name="contacto"),
    path('clinica/',clinica,name="clinica"),
    path('doctores/',doctores,name="doctores"),
    path('Sesion/',sesion,name="sesion"),
    path('Formulario/',formulario,name="formulario"),
    path('citas/',citas,name="citas"),
]