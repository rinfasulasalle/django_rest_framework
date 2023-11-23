# models/dropdowns.py
from django.db import models

class DropdownRoles(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.rol

class DropdownRolProyecto(models.Model):
    id = models.AutoField(primary_key=True)
    rol_titulo = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.rol_titulo

class DropdownAreas(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.area

class DropdownTipoContrato(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_contrato = models.CharField(max_length=100)
    dleg = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_contrato

class DropdownContratoOpcion(models.Model):
    id = models.AutoField(primary_key=True)
    opcion_contrato = models.CharField(max_length=100)

    def __str__(self):
        return self.opcion_contrato

class DropdownEmpleoTipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_empleo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_empleo

class DropdownEmpleoSituacion(models.Model):
    id = models.AutoField(primary_key=True)
    situacion_empleo = models.CharField(max_length=100)

    def __str__(self):
        return self.situacion_empleo

class DropdownProyecto(models.Model):
    id = models.AutoField(primary_key=True)
    proyecto = models.CharField(max_length=100)

    def __str__(self):
        return self.proyecto

class DropdownNivelEducativo(models.Model):
    id = models.AutoField(primary_key=True)
    nivel_educativo = models.CharField(max_length=255)

    def __str__(self):
        return self.nivel_educativo

class DropdownSituacionesEspeciales(models.Model):
    id = models.AutoField(primary_key=True)
    situacion_especial = models.CharField(max_length=255)

    def __str__(self):
        return self.situacion_especial

class DropdownRegimenLaboral(models.Model):
    id = models.AutoField(primary_key=True)
    regimen_laboral = models.CharField(max_length=255)

    def __str__(self):
        return self.regimen_laboral

class DropdownRegimenAseguramiento(models.Model):
    id = models.AutoField(primary_key=True)
    regimen_aseguramiento = models.CharField(max_length=255)

    def __str__(self):
        return self.regimen_aseguramiento

class DropdownInstituciones(models.Model):
    id = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=255)

    def __str__(self):
        return self.institucion

class DropdownCarreras(models.Model):
    id = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=255)

    def __str__(self):
        return self.carrera

class DropdownCapacitaciones(models.Model):
    id = models.AutoField(primary_key=True)
    capacitacion = models.CharField(max_length=255)

    def __str__(self):
        return self.capacitacion

class DropdownEspecializaciones(models.Model):
    id = models.AutoField(primary_key=True)
    especializacion = models.CharField(max_length=255)

    def __str__(self):
        return self.especializacion

class DropdownSedes(models.Model):
    id = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=255)

    def __str__(self):
        return self.sede
