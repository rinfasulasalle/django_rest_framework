# models/cuenta_bancaria.py
from django.db import models
from .trabajador import Trabajador  # Asegúrate de importar el modelo correcto

class CuentaBancaria(models.Model):
    id = models.AutoField(primary_key=True)
    #usuario_id = models.CharField(max_length=20)
    cuenta_bancaria_sueldo_codigo_cci = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_sueldo_codigo = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_sueldo_banco = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_codigo_cci = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_codigo = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_banco = models.CharField(max_length=255, null=True, blank=True)

    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cuenta Bancaria: {self.id} - {self.trabajador.usuario_relacionado.id}"

