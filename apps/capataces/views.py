
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Capataz
from .forms import CapatazForm


def listadocapataces(request):
    resultados = None
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        resultados = Capataz.objects.filter(
                    Q(apellido__icontains=parametro) |
                    Q(nombre__contains=parametro)
                ).order_by('apellido')

    return render(
        request,
        "capataces/listadocapataces.html",
        {
            "resultados": resultados
        }
    )


def nuevocapataz(request):
    if request.POST:
        form = CapatazForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA GRABADO EL CAPATAZ")
            return redirect('/capataces/listado')
        else:
            return render(request, 'capataces/capataz_edit.html', {"form": form})
    else:
        form = CapatazForm()
        return render(request, 'capataces/capataz_edit.html', {"form": form})


def editarcapataz(request, pk):
    consulta = Capataz.objects.get(pk=pk)
    if request.POST:
        form = CapatazForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO EL CAPATAZ")
            return redirect('/capataces/listado')
        else:
            return render(request, 'capataces/capataz_edit.html', {"form": form})
    else:
        form = CapatazForm(instance=consulta)
        return render(request,
            'capataces/capataz_edit.html',
            {"form": form}
        )


# Create your views here.
