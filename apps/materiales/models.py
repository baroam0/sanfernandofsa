
from django.db import models


class Material(models.Model):
    UNIDAD = 'UN'
    KILO = 'KG'
    METROCUAD = 'M2'
    METROCUB = 'M3'
    TONELADA = 'TN'
    UNIDADES = [
        (UNIDAD, 'Unidad'),
        (KILO, 'Kilo'),
        (METROCUAD, 'Metro Cuadrado'),
        (METROCUB, 'Metro Cubico'),
        (TONELADA, 'Tonelada'),
    ]
    descripcion = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    
    unidad = models.CharField(
        max_length=2,
        choices=UNIDADES,
        default=UNIDAD,
    )

    cantidad = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Materiales"


# Create your models here.
