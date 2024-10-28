from django.contrib import admin
from app1.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['nombre_usuario','nombre','apellido','edad']

admin.site.register(Usuario,UsuarioAdmin)


# Register your models here.
