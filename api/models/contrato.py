# models/contrato.py
from django.db import models
from .dropdowns import (
    DropdownTipoContrato,
    DropdownContratoOpcion,
    DropdownEmpleoTipo,
    DropdownEmpleoSituacion,
    DropdownAreas,
    DropdownProyecto,
    DropdownRolProyecto,
)
from .trabajador import Trabajador  # Asegúrate de importar el modelo correcto

class Contrato(models.Model):
    id = models.AutoField(primary_key=True)
    #usuario_id = models.CharField(max_length=20)
    id_contrato_tipo = models.ForeignKey(DropdownTipoContrato, on_delete=models.CASCADE)
    id_contrato_opcion = models.ForeignKey(DropdownContratoOpcion, on_delete=models.CASCADE)
    id_empleo_tipo = models.ForeignKey(DropdownEmpleoTipo, on_delete=models.CASCADE)
    id_empleo_situacion = models.ForeignKey(DropdownEmpleoSituacion, on_delete=models.CASCADE)
    id_empleo_area = models.ForeignKey(DropdownAreas, on_delete=models.CASCADE)
    id_empleo_proyecto = models.ForeignKey(DropdownProyecto, on_delete=models.CASCADE)
    id_empleo_proyecto_rol = models.ForeignKey(DropdownRolProyecto, on_delete=models.CASCADE)
    empleo_departamento = models.CharField(max_length=100, null=True, default=None)
    empleo_cargo = models.CharField(max_length=100, null=True, default=None)

    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contrato: {self.id} - {self.trabajador.usuario_relacionado.id}"