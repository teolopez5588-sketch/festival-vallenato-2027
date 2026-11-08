
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db import IntegrityError, transaction

from .models import Edicion, Categoria, Votacion, Opcion, Voto
from django.http import JsonResponse
from django.views.decorators.http import require_GET



def inicio(request):
    ediciones = Edicion.objects.filter(
        activa=True
    ).order_by("-anio")

    categorias = (
        Categoria.objects
        .filter(activa=True, edicion__activa=True)
        .select_related("edicion")
        .prefetch_related("votaciones__opciones")
        .order_by("nombre")
    )

    return render(
        request,
        "inicio.html",
        {
            "ediciones": ediciones,
            "categorias": categorias,
        }
    )


def registro(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect("inicio")
    else:
        formulario = UserCreationForm()

    return render(
        request,
        "registro.html",
        {"formulario": formulario}
    )


@login_required
def votar(request, votacion_id):

    # Solo se permiten solicitudes POST.
    if request.method != "POST":
        messages.error(
            request,
            "Debes enviar el formulario para registrar tu voto."
        )
        return redirect("inicio")

    votacion = get_object_or_404(
        Votacion.objects.select_related(
            "categoria__edicion"
        ),
        pk=votacion_id
    )

    categoria = votacion.categoria
    edicion = categoria.edicion
    ahora = timezone.now()

    # Comprobar que la votación, categoría y edición estén activas.
    if not votacion.activa or not categoria.activa or not edicion.activa:
        messages.error(
            request,
            "Esta votación no está disponible."
        )
        return redirect("inicio")

    # Comprobar las fechas de la votación.
    if votacion.fecha_inicio and ahora < votacion.fecha_inicio:
        messages.error(
            request,
            "Esta votación todavía no ha comenzado."
        )
        return redirect("inicio")

    if votacion.fecha_fin and ahora > votacion.fecha_fin:
        messages.error(
            request,
            "Esta votación ya ha finalizado."
        )
        return redirect("inicio")

    # Validar que la opción pertenezca a esta votación.
    opcion = get_object_or_404(
        Opcion,
        pk=request.POST.get("opcion"),
        votacion=votacion,
        activa=True
    )

    try:
        with transaction.atomic():

            # Bloquear temporalmente la categoría para coordinar
            # solicitudes simultáneas sobre la misma categoría.
            Categoria.objects.select_for_update().get(
                pk=categoria.pk
            )

            # La regla es un voto por usuario, categoría y edición.
            voto_existente = Voto.objects.filter(
                usuario=request.user,
                categoria=categoria,
                edicion=edicion
            ).exists()

            if voto_existente:
                messages.warning(
                    request,
                    "Ya registraste un voto en esta categoría "
                    "para esta edición. Puedes participar en otras categorías."
                )
                return redirect("inicio")

            # Registrar el voto con todas las relaciones.
            Voto.objects.create(
                usuario=request.user,
                categoria=categoria,
                edicion=edicion,
                votacion=votacion,
                opcion=opcion
            )

        messages.success(
            request,
            f"Tu voto por {opcion.nombre} se registró correctamente."
        )

    except IntegrityError:
        # La restricción única de MySQL es la protección final
        # frente a cualquier intento de duplicación.
        messages.warning(
            request,
            "Ya existe un voto tuyo en esta categoría para esta edición."
        )

    return redirect("inicio")


@login_required
def historial(request):
    votos = (
        Voto.objects
        .filter(usuario=request.user)
        .select_related(
            "edicion",
            "categoria",
            "votacion",
            "opcion"
        )
        .order_by("-fecha")
    )

    return render(
        request,
        "historial.html",
        {"votos": votos}
    )


@require_GET
def api_categorias(request):
    categorias = (
        Categoria.objects
        .filter(
            activa=True,
            edicion__activa=True
        )
        .select_related("edicion")
        .prefetch_related("votaciones__opciones")
        .order_by("nombre")
    )

    resultado = []

    for categoria in categorias:
        votaciones = []

        for votacion in categoria.votaciones.filter(activa=True):
            opciones = [
                {
                    "id": opcion.id,
                    "nombre": opcion.nombre,
                    "descripcion": opcion.descripcion,
                    "imagen_url": opcion.imagen_url
                }
                for opcion in votacion.opciones.filter(activa=True)
            ]

            votaciones.append({
                "id": votacion.id,
                "titulo": votacion.titulo,
                "descripcion": votacion.descripcion,
                "opciones": opciones
            })

        resultado.append({
            "id": categoria.id,
            "nombre": categoria.nombre,
            "descripcion": categoria.descripcion,
            "edicion": {
                "id": categoria.edicion.id,
                "anio": categoria.edicion.anio,
                "nombre": categoria.edicion.nombre
            },
            "votaciones": votaciones
        })

    return JsonResponse({
        "total_categorias": len(resultado),
        "categorias": resultado
    })

