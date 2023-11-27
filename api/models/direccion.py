# models/direccion.py
from django.db import models
from .trabajador import Trabajador  # Asegúrate de importar el modelo correcto

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    #usuario_id = models.CharField(max_length=20)
    direccion_pais = models.CharField(max_length=255)
    direccion_departamento = models.CharField(max_length=255)
    direccion_provincia = models.CharField(max_length=255)
    direccion_distrito = models.CharField(max_length=255)
    direccion_detalle = models.CharField(max_length=255)

    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Direccion: {self.id} - {self.trabajador.usuario_relacionado.id}"

