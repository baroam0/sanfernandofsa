"""sanfernandofsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path

from .views import listado, nuevo, editar

urlpatterns = [
    path('listado/', listado, name='listado'),
    path('nuevo/', listado, name='nuevo'),
    path('editar/<int:pk>', editar, name='editar')
=======

from django.urls import path

from .views import listadomaterial, nuevomaterial, editarmaterial

urlpatterns = [
    path('listado/', listadomaterial, name='listado'),
    path('nuevo/', nuevomaterial, name='nuevo'),
    path('editar/<int:pk>', editarmaterial, name='editar'),
>>>>>>> 011c1136b6cac864ccb0deff78b40c50555b83bf
]
