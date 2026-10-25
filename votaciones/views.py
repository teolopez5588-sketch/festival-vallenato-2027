
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db import IntegrityError, transaction

from .models import Edicion, Categoria, Votacion, Opcion, Voto


def inicio(request):
    ediciones = Edicion.objects.filter(activa=True).order_by("-anio")

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
    votacion = get_object_or_404(
        Votacion.objects.select_related(
            "categoria__edicion"
        ),
        pk=votacion_id
    )

    ahora = timezone.now()

    if (
        not votacion.activa
        or not votacion.categoria.activa
        or not votacion.categoria.edicion.activa
    ):
        messages.error(request, "Esta votación no está disponible.")
        return redirect("inicio")

    if votacion.fecha_inicio and ahora < votacion.fecha_inicio:
        messages.error(request, "Esta votación todavía no ha comenzado.")
        return redirect("inicio")

    if votacion.fecha_fin and ahora > votacion.fecha_fin:
        messages.error(request, "Esta votación ya ha finalizado.")
        return redirect("inicio")

    if Voto.objects.filter(
        usuario=request.user,
        votacion=votacion
    ).exists():
        messages.warning(
            request,
            "Ya registraste un voto en esta votación."
        )
        return redirect("inicio")

    if request.method != "POST":
        return redirect("inicio")

    opcion_id = request.POST.get("opcion")

    opcion = get_object_or_404(
        Opcion,
        pk=opcion_id,
        votacion=votacion,
        activa=True
    )

    try:
        with transaction.atomic():
            Voto.objects.create(
                usuario=request.user,
                votacion=votacion,
                opcion=opcion
            )

        messages.success(
            request,
            f"Tu voto por {opcion.nombre} se registró correctamente."
        )

    except IntegrityError:
        messages.warning(
            request,
            "Ya existe un voto tuyo para esta votación."
        )

    return redirect("inicio")
