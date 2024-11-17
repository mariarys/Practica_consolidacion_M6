from django.urls import path
from . import views
from .views import IndexPageView
from django.contrib.auth.views import LogoutView  # Importa LogoutView desde django.contrib.auth.views

urlpatterns = [
    path('', IndexPageView.as_view(), name='vehiculo'),
    path('add/', views.ingresar_vehiculo, name='add_vehiculo'), 
    path('listado/', views.lista_vehiculos, name='listado_vehiculo'), 
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('addusuario/', views.add_usuario, name='addusuario'), 
]
