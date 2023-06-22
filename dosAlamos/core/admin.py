from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Rol, Comuna, HoraTomada, FichaMedica

class RolInline(admin.TabularInline):
    model = Rol
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = (RolInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Rol)
admin.site.register(Comuna)
admin.site.register(HoraTomada)
admin.site.register(FichaMedica)