from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Rol(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rol', null=True)
    nombreRol = models.CharField(max_length=25, verbose_name='El nombre del rol de usuario')

    def __str__(self):
        return self.nombreRol

def set_default_rol(sender, instance, created, **kwargs):
    if created:
        Rol.objects.get_or_create(user=instance, nombreRol='Paciente')

models.signals.post_save.connect(set_default_rol, sender=User)


class Comuna(models.Model):
    nombreComuna = models.CharField(max_length=25, verbose_name='El nombre de la comuna')

    def __str__(self):
        return self.nombreComuna
    

class CustomUser(AbstractUser):
    edad = models.IntegerField(blank=True, null=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )