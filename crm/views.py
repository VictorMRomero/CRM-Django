from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Cliente
from django.shortcuts import get_object_or_404



# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:

        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except:
                return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Ya existe el usuario'
            })
        else:
            return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Contraseña no es igual'
            })
        
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {
                'error': 'Credenciales inválidas'
            })
    else:
        return render(request, 'login.html')

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
