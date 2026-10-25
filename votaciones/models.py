
from django.db import models


class Edicion(models.Model):
    anio = models.PositiveIntegerField(
        unique=True,
        verbose_name="Año"
    )
    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre de la edición"
    )
    fecha_inicio = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de inicio"
    )
    fecha_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de finalización"
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    activa = models.BooleanField(
        default=True,
        verbose_name="Activa"
    )

    class Meta:
        verbose_name = "Edición"
        verbose_name_plural = "Ediciones"
        ordering = ["-anio"]

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


class Categoria(models.Model):
    edicion = models.ForeignKey(
        Edicion,
        on_delete=models.CASCADE,
        related_name="categorias",
        verbose_name="Edición"
    )
    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre"
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    activa = models.BooleanField(
        default=True,
        verbose_name="Activa"
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]
        constraints = [
            models.UniqueConstraint(
                fields=["edicion", "nombre"],
                name="categoria_unica_por_edicion"
            )
        ]

    def __str__(self):
        return f"{self.nombre} - {self.edicion.anio}"


class Votacion(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="votaciones",
        verbose_name="Categoría"
    )
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título"
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    fecha_inicio = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de inicio"
    )
    fecha_fin = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de finalización"
    )
    activa = models.BooleanField(
        default=True,
        verbose_name="Activa"
    )

    class Meta:
        verbose_name = "Votación"
        verbose_name_plural = "Votaciones"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo


class Opcion(models.Model):
    votacion = models.ForeignKey(
        Votacion,
        on_delete=models.CASCADE,
        related_name="opciones",
        verbose_name="Votación"
    )
    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre de la opción"
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    imagen_url = models.URLField(
        blank=True,
        verbose_name="URL de imagen"
    )
    activa = models.BooleanField(
        default=True,
        verbose_name="Activa"
    )

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"
        ordering = ["nombre"]
        constraints = [
            models.UniqueConstraint(
                fields=["votacion", "nombre"],
                name="opcion_unica_por_votacion"
            )
        ]

    def __str__(self):
        return f"{self.nombre} - {self.votacion.titulo}"


from django.conf import settings


class Voto(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="votos"
    )

    votacion = models.ForeignKey(
        Votacion,
        on_delete=models.CASCADE,
        related_name="votos"
    )

    opcion = models.ForeignKey(
        Opcion,
        on_delete=models.CASCADE,
        related_name="votos"
    )

    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "votacion"],
                name="un_voto_por_usuario_votacion"
            )
        ]

    def __str__(self):
        return f"{self.usuario} - {self.votacion.titulo} - {self.opcion.nombre}"
