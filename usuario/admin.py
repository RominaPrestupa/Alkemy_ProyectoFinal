from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuario.models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    search_fields = ['username']
