# models/sueldo.py
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .trabajador import Trabajador
from .datos_globales import DatosGlobales
from datetime import datetime

class Sueldo(models.Model):
    id = models.AutoField(primary_key=True)
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, related_name='sueldo')
    sueldo_valor_basico = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_asigfam_porcentaje = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0)# 0 o 0.1
    sueldo_asignacion_familiar = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0)# = sueldo_asigfam_porcentaje * rmv
    sueldo_bono_porcentaje = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    sueldo_monto_bono = models.DecimalField(max_digits=20, decimal_places=2, default=0) # = sueldo_bono_porcentaje * sueldo_valor_basico
    sueldo_mensual = models.DecimalField(max_digits=20, decimal_places=2, default=0) # = sueldo_valor_basico + sueldo_asignacion_familiar + sueldo_monto_bono
    sueldo_anual = models.DecimalField(max_digits=20, decimal_places=2, default=0) # = sueldo_mensual * 14
    activo = models.BooleanField(default=True)
    # ------------------------------------------------------------------
    def calcular_asignacion_familiar(self, rmv):
        if self.sueldo_asigfam_porcentaje:
            self.sueldo_asignacion_familiar = self.sueldo_asigfam_porcentaje * rmv

    def calcular_monto_bono(self):
        if self.sueldo_valor_basico:
            self.sueldo_monto_bono = self.sueldo_bono_porcentaje * self.sueldo_valor_basico

    def calcular_sueldo_mensual(self):
        if self.sueldo_valor_basico:
            self.sueldo_mensual = self.sueldo_valor_basico + self.sueldo_asignacion_familiar + self.sueldo_monto_bono

    def calcular_sueldo_anual(self):
        if self.sueldo_mensual:
            self.sueldo_anual = self.sueldo_mensual * 14

    def __str__(self):
        return f"Sueldo: {self.id} - {self.trabajador.usuario_relacionado.id}"

# Señal para calcular campos antes de guardar
@receiver(pre_save, sender=Sueldo)
def validar_y_calcular_campos(sender, instance, **kwargs):
    # Obtener la RMV del año actual
    rmv = DatosGlobales.objects.get(id=1, variable='RMV', anio=datetime.now().year).valor

    # Validar que sueldo_valor_basico sea mayor que la RMV
    if instance.sueldo_valor_basico <= rmv-1:
        raise ValueError("El sueldo básico debe ser mayor que la Remuneración Mínima Vital del año actual")

    # Calcular campos relacionados con el sueldo
    instance.calcular_asignacion_familiar(rmv)
    instance.calcular_monto_bono()
    instance.calcular_sueldo_mensual()
    instance.calcular_sueldo_anual()


