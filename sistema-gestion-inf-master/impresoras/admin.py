from impresoras.models import Impresora, marca_modelo, Conexion, Tipo_impresion, Estado
from django.contrib import admin

admin.site.register(Impresora)
admin.site.register(marca_modelo)
admin.site.register(Conexion)
admin.site.register(Tipo_impresion)
admin.site.register(Estado)