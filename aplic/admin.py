from django.contrib import admin
from aplic.models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('id','identificacion','nombreUsuario','nombres','apellidos')
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(Parametro)
admin.site.register(ValorParametro)