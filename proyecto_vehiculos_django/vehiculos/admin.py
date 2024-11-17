from django.contrib import admin
from .models import Vehiculo

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'rating', 'fecha_creacion', 'fecha_modificacion')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_filter = ('marca', 'categoria')


admin.site.register(Vehiculo, VehiculoAdmin)
