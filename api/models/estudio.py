# models/estudio.py
from django.db import models
from .trabajador import Trabajador  # Asegúrate de importar el modelo correcto
from .dropdowns import (
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

class Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    #usuario_id = models.CharField(max_length=20)
    id_estudio_nivel_educativo = models.ForeignKey(DropdownNivelEducativo, on_delete=models.CASCADE)
    id_estudio_situacion_especial = models.ForeignKey(DropdownSituacionesEspeciales, on_delete=models.CASCADE)
    id_regimen_laboral = models.ForeignKey(DropdownRegimenLaboral, on_delete=models.CASCADE)
    id_regimen_aseguramiento = models.ForeignKey(DropdownRegimenAseguramiento, on_delete=models.CASCADE)
    id_institucion = models.ForeignKey(DropdownInstituciones, on_delete=models.CASCADE)
    id_carrera_educativa = models.ForeignKey(DropdownCarreras, on_delete=models.CASCADE)
    id_estudio_capacitacion = models.ForeignKey(DropdownCapacitaciones, on_delete=models.CASCADE)
    id_estudio_especializacion = models.ForeignKey(DropdownEspecializaciones, on_delete=models.CASCADE)
    estudio_fecha_colegiatura = models.DateField(null=True, blank=True)  # Puede ser nulo si no está colegiado
    id_sede_colegiatura = models.ForeignKey(DropdownSedes, on_delete=models.CASCADE)
    estudio_condicion = models.CharField(
        max_length=15,
        choices=[
            ('Habilitado', 'Habilitado'),
            ('No habilitado', 'No habilitado'),
            ('XXXXX', 'XXXXX'),
        ],
        default='XXXXX'
    )

    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Estudio: {self.id} - {self.trabajador.usuario_relacionado.id}"

