# models/sueldo.py
from django.db import models
from .trabajador import Trabajador  # Asegúrate de importar el modelo correcto

class Sueldo(models.Model):
    id = models.AutoField(primary_key=True)
    #usuario_id = models.CharField(max_length=20)
    sueldo_valor_basico = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_asigfam_porcentaje = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    sueldo_asignacion_familiar = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    sueldo_bono_porcentaje = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    sueldo_monto_bono = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_mensual = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_anual = models.DecimalField(max_digits=20, decimal_places=2)

    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sueldo: {self.id} - {self.trabajador.usuario_relacionado.id}"

