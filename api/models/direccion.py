from django.db import models
from .trabajador import Trabajador

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, related_name='direccion')
    direccion_pais = models.CharField(max_length=255)
    direccion_departamento = models.CharField(max_length=255)
    direccion_provincia = models.CharField(max_length=255)
    direccion_distrito = models.CharField(max_length=255)
    direccion_detalle = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return f"Direccion: {self.id} - {self.trabajador.usuario_relacionado.id}"
