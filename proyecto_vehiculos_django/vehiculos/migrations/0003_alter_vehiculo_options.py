# Generated by Django 4.0.5 on 2024-11-17 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Puede visualizar catálogo de vehículos'), ('agregar_vehiculo', 'Puede agregar vehículos')], 'verbose_name': 'Vehiculo', 'verbose_name_plural': 'Vehiculos'},
        ),
    ]
