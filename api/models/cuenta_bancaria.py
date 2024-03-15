# models/cuenta_bancaria.py
from django.db import models
from .trabajador import Trabajador

class CuentaBancaria(models.Model):
    id = models.AutoField(primary_key=True)
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, related_name='cuenta_bancaria')
    cuenta_bancaria_sueldo_codigo_cci = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_sueldo_codigo = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_sueldo_banco = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_codigo_cci = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_codigo = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_banco = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Cuenta Bancaria: {self.id} - {self.trabajador.usuario_relacionado.id}"

