
from django.contrib import admin
from .models import Edicion, Categoria, Votacion, Opcion, Voto


@admin.register(Edicion)
class EdicionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "anio", "fecha_inicio", "fecha_fin", "activa")
    list_filter = ("activa", "anio")
    search_fields = ("nombre", "descripcion")
    ordering = ("-anio",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edicion", "activa")
    list_filter = ("edicion", "activa")
    search_fields = ("nombre", "descripcion")


@admin.register(Votacion)
class VotacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "activa", "fecha_inicio", "fecha_fin")
    list_filter = ("activa", "categoria")
    search_fields = ("titulo", "descripcion")


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "votacion", "activa")
    list_filter = ("activa", "votacion")
    search_fields = ("nombre", "descripcion")


@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "votacion", "opcion", "fecha")
    list_filter = ("votacion", "fecha")
    search_fields = ("usuario__username", "opcion__nombre")
    readonly_fields = ("usuario", "votacion", "opcion", "fecha")
