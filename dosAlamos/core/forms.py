from django import forms
from .models import FichaMedica

class FormFicha(forms.ModelForm):
    class Meta:
        model = FichaMedica
        fields = ['hora_tomada','nombrePaciente','apellidoPaciente','correoPaciente','motivo','diagnostico','medicamentos']