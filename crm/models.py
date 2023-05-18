from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    acciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre