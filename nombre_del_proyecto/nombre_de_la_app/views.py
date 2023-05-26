from django.shortcuts import render, redirect
from .models import TipoDocumento

def inicio(request):
    return render(request, 'nombre_de_la_app/inicio.html')

def crear_tipodocumento(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        tipodocumento = TipoDocumento(nombre=nombre, descripcion=descripcion)
        tipodocumento.save()
        return redirect('lista_tipodocumentos')
    return render(request, 'nombre_de_la_app/crear_tipodocumento.html')

def lista_tipodocumentos(request):
    tipodocumentos = TipoDocumento.objects.all()
    return render(request, 'nombre_de_la_app/lista_tipodocumentos.html', {'tipodocumentos': tipodocumentos})

def actualizar_tipodocumento(request, tipodocumento_id):
    try:
        tipodocumento = TipoDocumento.objects.get(id=tipodocumento_id)
    except TipoDocumento.DoesNotExist:
        # Manejar la situación si el documento no existe
        return redirect('lista_tipodocumentos')

    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        tipodocumento.nombre = nombre
        tipodocumento.descripcion = descripcion
        tipodocumento.save()
        return redirect('lista_tipodocumentos')

    return render(request, 'nombre_de_la_app/actualizar_tipodocumento.html', {'tipodocumento': tipodocumento})

def eliminar_tipodocumento(request, tipodocumento_id):
    try:
        tipodocumento = TipoDocumento.objects.get(id=tipodocumento_id)
    except TipoDocumento.DoesNotExist:
        return redirect('lista_tipodocumentos')

    if request.method == 'POST':
        tipodocumento.delete()
        return redirect('lista_tipodocumentos')

    return render(request, 'nombre_de_la_app/eliminar_tipodocumento.html', {'tipodocumento': tipodocumento})