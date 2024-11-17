from django.db import models

class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]
    
    marca = models.CharField(
        max_length=20,
        choices=MARCAS,
        default='Ford',
    )
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='Particular',
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def rating(self):
        if self.precio < 10000:
            return "Bajo"
        elif 10000 <= self.precio <= 30000:
            return "Medio"
        else:
            return "Alto"

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
        permissions = [
            ("visualizar_catalogo", "Puede visualizar catálogo de vehículos"),
            ("agregar_vehiculo", "Puede agregar vehículos")
        ]
        

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.serial_carroceria}'

