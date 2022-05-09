
from django.http import JsonResponse

from apps.materiales.models import Material


def modificacantidadmaterial(material_id, cantidadingresada):
    material = Material.objects.get(pk=material_id)
    material.cantidad = float(material.cantidad) - float(cantidadingresada)
    material.save()
    cantidad = Material.objects.get(pk=material_id)
    return cantidad.cantidad


def validacantidad(material_id, cantidad):
    material = Material.objects.get(pk=material_id)
    deposito = DepositoCantidad.objects.get(material=material)

    if float(cantidad) < float(deposito.cantidad):
        return 1
    else:
        return 0


def restauracantidad(material_id, cantidadingresada):
    material = Material.objects.get(pk=material_id)
    material.cantidad = float(material.cantidad) + float(cantidadingresada)
    material.save()
    return material.pk