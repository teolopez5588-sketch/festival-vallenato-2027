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
    search_fields = ("nombre", "descripcion", "edicion__nombre")


@admin.register(Votacion)
class VotacionAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "activa",
        "fecha_inicio",
        "fecha_fin",
    )
    list_filter = ("activa", "categoria")
    search_fields = (
        "titulo",
        "descripcion",
        "categoria__nombre",
    )


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "votacion", "activa")
    list_filter = ("activa", "votacion")
    search_fields = ("nombre", "descripcion", "votacion__titulo")


@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "edicion",
        "categoria",
        "votacion",
        "opcion",
        "fecha",
    )

    list_filter = (
        "edicion",
        "categoria",
        "votacion",
        "fecha",
    )

    search_fields = (
        "usuario__username",
        "usuario__first_name",
        "usuario__last_name",
        "opcion__nombre",
        "categoria__nombre",
        "votacion__titulo",
        "edicion__nombre",
    )

    readonly_fields = (
        "usuario",
        "edicion",
        "categoria",
        "votacion",
        "opcion",
        "fecha",
    )

    list_select_related = (
        "usuario",
        "edicion",
        "categoria",
        "votacion",
        "opcion",
    )

    date_hierarchy = "fecha"
    ordering = ("-fecha",)
    list_per_page = 25