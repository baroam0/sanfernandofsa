
from apps.materiales.models import Material, Unidad

archivo = open("materiales.txt", "r")

materiales = archivo.readlines()

materiales = list(dict.fromkeys(materiales))

print("Grabando...")

unidad = Unidad.objects.get(pk=1)


for material in materiales:
    if material != "":
        grabar = Material(descripcion=str(material), cantidad=0, unidad=unidad)
        grabar.save()

