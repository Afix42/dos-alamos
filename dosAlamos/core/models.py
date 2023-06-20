from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rol', null=True)
    nombreRol = models.CharField(max_length=25, verbose_name='El nombre del rol de usuario')

    def __str__(self):
        return self.nombreRol

def set_default_rol(sender, instance, created, **kwargs):
    if created:
        Rol.objects.get_or_create(user=instance, nombreRol='Paciente')

models.signals.post_save.connect(set_default_rol, sender=User)


    