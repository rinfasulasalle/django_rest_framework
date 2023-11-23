# admin.py
from django.contrib import admin
from .models import (
    Usuario,
    Trabajador,
    Sueldo,
    Contrato,
    CuentaBancaria,
    Direccion,
    Estudio,
    # Asegúrate de importar otros modelos si los tienes
)

admin.site.register(Usuario)
admin.site.register(Trabajador)
admin.site.register(Sueldo)
admin.site.register(Contrato)
admin.site.register(CuentaBancaria)
admin.site.register(Direccion)
admin.site.register(Estudio)
# Registra otros modelos si los tienes
