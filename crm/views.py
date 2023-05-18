from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Cliente
from django.shortcuts import get_object_or_404



# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {
        'clientes': clientes
    })

def nuevocliente(request):
    if request.method == 'GET':
        return render(request, 'nuevo-cliente.html')
    else:
        Cliente.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            correo=request.POST['correo'],
            telefono=request.POST['telefono'],
            acciones=request.POST['acciones']
        )

        return redirect('index')


def editarcliente(request, idcliente):
    cliente = get_object_or_404(Cliente, id=idcliente)
    accion = request.POST.get('accion')

    if accion == 'Guardar Cambios':
        # Lógica para guardar los cambios del cliente
        print(request.POST)
        cliente.nombre = request.POST.get('nombre', cliente.nombre)
        cliente.apellido = request.POST.get('apellido', cliente.apellido)
        cliente.correo = request.POST.get('correo', cliente.correo)
        cliente.telefono = request.POST.get('telefono', cliente.telefono)
        cliente.acciones = request.POST.get('acciones', cliente.acciones)
        cliente.save()
        return redirect('index')
            
    elif accion == 'Eliminar':
        cliente.delete()
        return redirect('index')

    
   
    
    return render(request, 'editar-cliente.html', {
        'cliente': cliente
    })
