from django.db import models
from pyexpat import model 

# Create your models here.
# Marca: Fiat, Chevrolet, Ford y Toyota # modelo
# Serial Carroceria
# Serial Motor
# Categoría: Particular, trasporte y carga
# Precio
# fecha de creación
# fecha de modificación
class VehiculoModel(models.Model): # Opciones por Marca
    MARCA = (
        ('FIAT', 'Fiat'),
        ('FORD', 'Ford'),
        ('CHEVROLET', 'Chevrolet'),
        ('TOYOTA', 'Toyota'),
    )
    # Opciones por Marca
    CATEGORIA = (
        ('PARTICULAR', 'Particular'), 
        ('TRASPORTE', 'Transporte'), 
        ('CARGA', 'Carga'),
    )
    # Campos del modelo
    marca = models.CharField(max_length=20, choices=MARCA, default='FORD')
    modelo = models.TextField(max_length=100, verbose_name='Modelo')
    serial_carroceria = models.CharField(max_length=50) 
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA,
    default='PARTICULAR')
    precio = models.FloatField()
    f_creacion = models.DateTimeField(auto_now_add=True) 
    f_modificado = models.DateTimeField(auto_now = True)
    def __str__(self): return f'{self.marca} {self.modelo}'