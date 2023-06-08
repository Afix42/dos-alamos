from django.contrib import admin
from django.urls import path
from .views import home, Servicios, Registro, contacto, clinica


urlpatterns = [
    path('', home, name='home'),
    path('Servicios/',Servicios,name="Servicios"),
    path('Registro/',Registro,name="Registro"),
    path('contacto/',contacto,name="contacto"),
    path('clinica/',clinica,name="clinica"),
]