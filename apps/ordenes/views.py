

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import DetalleOrden, Orden
from apps.capataces.models import Capataz

from apps.materiales.forms import MaterialForm
from apps.materiales.models import Material, Unidad

from apps.obras.models import Obra

from apps.libs.funcionfecha import revertirfecha
from apps.libs.helper import modificacantidadmaterial, restauracantidad




def listadoorden(request):
    resultados = None
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        if parametro!="":
            if parametro.isnumeric():
                try:
                    resultados = Orden.objects.filter(
                        pk=int(parametro)
                    )
                except:
                    resultados=None
            else:
                resultados = Orden.objects.filter(
                    Q(obra__descripcion__icontains=parametro) |
                    Q(capataz__nombre__icontains=parametro) |
                    Q(capataz__apellido__icontains=parametro)
                    ).order_by("-pk")
        else:
            resultados = Orden.objects.all().order_by("-pk")

    return render(
        request,
        "ordenes/listadoorden.html",
        {
            "resultados": resultados
        }
    )


def nuevaorden(request):
    capataces = Capataz.objects.all()
    obras = Obra.objects.all().order_by("descripcion")

    return render(
        request,
        "ordenes/orden_nueva.html",
        {
            "capataces": capataces,
            "obras": obras
        }
    )


@csrf_exempt
def ajaxgrabarorden(request):
    fecha = request.POST["fecha"]
    fecha = revertirfecha(fecha)
    capataz = Capataz.objects.get(pk=int(request.POST["capataz"]))
    obra = Obra.objects.get(pk=int(request.POST["obra"]))

    arraymaterial = request.POST.getlist('arraymaterial[]')
    arraycantidad = request.POST.getlist('arraycantidad[]')

    orden=Orden(
        fecha=fecha,
        capataz=capataz,
        obra=obra
    )

    orden.save()
    orden = Orden.objects.latest("pk")

    for (material, cantidad) in zip(arraymaterial, arraycantidad):
        material = Material.objects.get(pk=int(material))

        detalleorden = DetalleOrden(
            orden=orden,
            material=material,
            cantidad=cantidad
        )

        modificacantidadmaterial(material.pk, cantidad)

        detalleorden.save()

    data = {
        "status": 200
    }

    return JsonResponse(data)


def editarorden(request, pk):
    capataces = Capataz.objects.all()
    obras = Obra.objects.all().order_by("descripcion")
    unidades = Unidad.objects.all()

    orden = Orden.objects.get(pk=pk)
    detallesorden = DetalleOrden.objects.filter(
        orden=orden
    )

    return render(
        request,
        "ordenes/orden_edit.html",
        {
            "orden": orden,
            "detallesorden": detallesorden,
            "capataces": capataces,
            "obras": obras,
            "unidades": unidades
        }
    )


@csrf_exempt
def ajaxgrabareditarorden(request,pk):
    detalleorden=DetalleOrden.objects.filter(orden=pk)

    for d in detalleorden:
        restauracantidad(d.material.pk, d.cantidad)
    
    detalleorden.delete()

    fecha = request.POST["fecha"]
    fecha = revertirfecha(fecha)
    capataz = Capataz.objects.get(pk=int(request.POST["capataz"]))
    obra = Obra.objects.get(pk=int(request.POST["obra"]))

    arraymaterial = request.POST.getlist('arraymaterial[]')
    #arrayunidad = request.POST.getlist('arrayunidad[]')
    arraycantidad = request.POST.getlist('arraycantidad[]')

    orden = Orden.objects.get(pk=pk)

    orden = Orden.objects.filter(pk=pk).update(
        fecha=fecha,
        capataz=capataz,
        obra=obra
    )
    obra.save()

    orden = Orden.objects.get(pk=pk)

    for (material, cantidad) in zip(arraymaterial, arraycantidad):
        material = Material.objects.get(pk=int(material))
        #unidad = Unidad.objects.get(materialpk=int(unidad))

        detalleorden = DetalleOrden(
            orden=orden,
            material=material,
            cantidad=cantidad,
        )
        
        modificacantidadmaterial(material.pk, cantidad)

        detalleorden.save()

    data = {
        "status": 200
    }

    return JsonResponse(data)


def imprimirorden(request,pk):
    orden = Orden.objects.get(pk=pk)
    detallesorden = DetalleOrden.objects.filter(orden=orden)

    return render(
        request,
        "ordenes/imprimirorden.html",
        {
            "orden": orden,
            "detallesorden": detallesorden
        }
    )

# Create your views here.
