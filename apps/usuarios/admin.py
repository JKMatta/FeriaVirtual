from django.contrib import admin
from .models import usuarios
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdmin(UserAdmin):
    fieldsets = (
        ('Credenciales', {
            'fields': ('username','password')}),
        ('Información personal', {
            "fields": ('email','first_name','last_name','direccion',)}),
        ('Permisos', {
            "fields": ('is_active','tipo_usuario')}),

    )

admin.site.register(usuarios,UserAdmin)