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
    DropdownRoles,
    DropdownRolProyecto,
    DropdownAreas,
    DropdownTipoContrato,
    DropdownContratoOpcion,
    DropdownEmpleoTipo,
    DropdownEmpleoSituacion,
    DropdownProyecto,
    DropdownNivelEducativo,
    DropdownSituacionesEspeciales,
    DropdownRegimenLaboral,
    DropdownRegimenAseguramiento,
    DropdownInstituciones,
    DropdownCarreras,
    DropdownCapacitaciones,
    DropdownEspecializaciones,
    DropdownSedes,
)

admin.site.register(Usuario)
admin.site.register(Trabajador)
admin.site.register(Sueldo)
admin.site.register(Contrato)
admin.site.register(CuentaBancaria)
admin.site.register(Direccion)
admin.site.register(Estudio)

# Registra los modelos de "dropdowns"
admin.site.register(DropdownRoles)
admin.site.register(DropdownRolProyecto)
admin.site.register(DropdownAreas)
admin.site.register(DropdownTipoContrato)
admin.site.register(DropdownContratoOpcion)
admin.site.register(DropdownEmpleoTipo)
admin.site.register(DropdownEmpleoSituacion)
admin.site.register(DropdownProyecto)
admin.site.register(DropdownNivelEducativo)
admin.site.register(DropdownSituacionesEspeciales)
admin.site.register(DropdownRegimenLaboral)
admin.site.register(DropdownRegimenAseguramiento)
admin.site.register(DropdownInstituciones)
admin.site.register(DropdownCarreras)
admin.site.register(DropdownCapacitaciones)
admin.site.register(DropdownEspecializaciones)
admin.site.register(DropdownSedes)
