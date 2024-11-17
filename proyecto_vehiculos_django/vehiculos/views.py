from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required
from .models import Vehiculo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Permission


class IndexPageView(TemplateView): 
    template_name = 'vehiculos/index.html'

@login_required
def ingresar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡El vehiculo se ha agregado exitosamente!")
            return redirect('vehiculo')  # Redirige a la página de inicio después de agregar el vehículo
    else:
        form = VehiculoForm()

    return render(request, 'vehiculos/add_vehiculo.html', {'form': form})

@login_required
def lista_vehiculos(request):
    # Obtiene todos los vehículos
    vehiculos = Vehiculo.objects.all()

    return render(request, 'vehiculos/listado_vehiculos.html', {
        'vehiculos': vehiculos,
    })

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticación exitosa
            user = form.get_user()
            login(request, user)
            messages.success(request, "¡Bienvenido de nuevo!")
            return redirect('vehiculo')
        else:
            messages.error(request, "Credenciales inválidas")
    else:
        form = AuthenticationForm()
    
    return render(request, 'vehiculos/login.html', {'form': form})

def add_usuario(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()

            permiso = Permission.objects.get(codename='visualizar_catalogo')
            usuario.user_permissions.add(permiso)

            return redirect('login')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'vehiculos/add_usuario.html', {'form': form})

