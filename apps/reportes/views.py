

from django.db.models import Count, Sum
from django.shortcuts import render

from apps.capataces.models import Capataz
from apps.obras.models import Obra
from apps.ordenes.models import Orden, DetalleOrden


def listadomaterialporcapataz(request):
    capataces = Capataz.objects.all().order_by('apellido')
    return render(
        request,
        "reportes/listado_materialporcapataz.html",
        {
            "capataces": capataces
        }
    )

def listadomaterialporobra(request):
    obras = Obra.objects.all()
    return render(
        request,
        "reportes/listado_materialporobra.html",
        {
            "obras": obras
        }
    )


def reportematerialporcapataz(request, pk):
    capataz = Capataz.objects.get(pk=pk)
    orden = Orden.objects.filter(capataz=capataz.pk)
    detallesordenes = DetalleOrden.objects.filter(
        orden__in=orden).values(
            'orden__obra__descripcion', 'material__descripcion', 'material__unidad__descripcion').annotate(cant=Sum('cantidad'))

    return render(
        request,
        "reportes/imprimirreportematerialporcapataz.html",
        {
            "capataz": capataz,
            "detallesordenes": detallesordenes,
        }
    )


def reportematerialporobra(request, pk):
    obra = Obra.objects.get(pk=pk)
    orden = Orden.objects.filter(obra=obra.pk)
    detallesordenes = DetalleOrden.objects.filter(orden=orden)

    detallesordenes = DetalleOrden.objects.filter(
        orden__in=orden).values(
            'material__unidad__descripcion','material__descripcion').annotate(
                cant=Sum('cantidad')).order_by('material')
    
    return render(
        request,
        "reportes/imprimirreportematerialporobra.html",
        {
            "detallesordenes": detallesordenes,
            "obra": obra
        }
    )
