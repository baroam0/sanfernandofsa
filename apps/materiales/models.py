
from django.db import models


<<<<<<< HEAD
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
=======
class Unidad(models.Model):
>>>>>>> 011c1136b6cac864ccb0deff78b40c50555b83bf
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
        verbose_name_plural = "Unidades"


class Material(models.Model):
    descripcion = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    cantidad = models.DecimalField(
        decimal_places=2, max_digits=10, null=True, blank=True)
    unidad = models.ForeignKey(Unidad, default=1, on_delete=models.CASCADE)

<<<<<<< HEAD
=======
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Materiales"

>>>>>>> 011c1136b6cac864ccb0deff78b40c50555b83bf
# Create your models here.
