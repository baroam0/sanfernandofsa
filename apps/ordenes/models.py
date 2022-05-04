
from django.db import models

from apps.capataces.models import Capataz
from apps.materiales.models import Material
from apps.obras.models import Obra


class Orden(models.Model):
    fecha = models.DateField(null=False)
    capataz = models.ForeignKey(Capataz, on_delete=models.CASCADE)
    obra = models.ForeignKey(
        Obra, on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.pk) + " - " + str(self.fecha)

    class Meta:
        verbose_name_plural="Orden"


class DetalleOrden(models.Model):
    orden = models.ForeignKey(
        Orden,
        on_delete=models.CASCADE
    )
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.orden)
    
    class Meta:
        verbose_name_plural="Detalles Ordenes"

# Create your models here.
