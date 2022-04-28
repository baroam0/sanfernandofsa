
from django.db import models


class Capataz(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False, unique=True)
    apellido = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.apellido + ', ' + self.nombre

    class Meta:
        verbose_name_plural = "Capataces"


# Create your models here.
