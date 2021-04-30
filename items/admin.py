from django.contrib import admin
from .models import Actividad,Carpeta

# Register your models here.
@admin.register(Actividad)
class ActAdmin(admin.ModelAdmin):
    pass


@admin.register(Carpeta)
class CarpetaAdmin(admin.ModelAdmin):
    pass