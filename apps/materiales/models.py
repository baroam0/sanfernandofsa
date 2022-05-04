
from django.db import models


class Unidad(models.Model):
    descripcion = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    
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

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Materiales"

# Create your models here.
