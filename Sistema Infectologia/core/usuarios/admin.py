from django.contrib import admin

# Register your models here.
from core.usuarios.models import Usuario

admin.site.register(Usuario)