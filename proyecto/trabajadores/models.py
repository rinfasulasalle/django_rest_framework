from django.db import models

class Usuario(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    id_usuario_rol = models.IntegerField()
    usuario_nombres = models.CharField(max_length=100)
    usuario_apellidos = models.CharField(max_length=100)
    usuario_correo = models.EmailField(unique=True)
    usuario_contrasenia = models.CharField(max_length=100)

    id_usuario_rol = models.ForeignKey('DropdownRoles', on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuario'
# --------------------------------------------------------------------
class DropdownRoles(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'dropdown_roles'
# --------------------------------------------------------------------
from django.db import models

class Trabajador(models.Model):
    usuario_id = models.OneToOneField('Usuario', on_delete=models.CASCADE, primary_key=True)
    trabajador_tipo_documento = models.CharField(max_length=100)
    trabajador_path_documento = models.CharField(max_length=255, default='PATH/noNe')
    trabajador_nacionalidad = models.CharField(max_length=100, default='No Especificado')
    trabajador_fecha_nacimiento = models.DateField()
    trabajador_ubigeo = models.CharField(max_length=255, default='No Especificado')
    trabajador_telefono = models.CharField(max_length=100)
    trabajador_sexo = models.CharField(max_length=20, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('No Especificado', 'No Especificado')], default='No Especificado')
    trabajador_estado_civil = models.CharField(max_length=20, choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Viudo', 'Viudo'), ('Divorciado', 'Divorciado'), ('Conviviente', 'Conviviente'), ('No Especificado', 'No Especificado')], default='No Especificado')
    trabajador_path_doc_estado_civil = models.CharField(max_length=255, default='PATH/noNe')
    trabajador_fecha_ingreso_sistema = models.DateField(null=True)  # Puede ser NULL según la lógica de tu aplicación
    trabajador_fecha_ingreso = models.DateField()
    trabajador_edad = models.IntegerField()  # Este campo se puede calcular en la lógica de tu aplicación
    trabajador_record = models.DecimalField(max_digits=20, decimal_places=2)
    trabajador_exp_previa = models.DecimalField(max_digits=20, decimal_places=2)
    trabajador_total_anios_exp = models.DecimalField(max_digits=20, decimal_places=2)
    
    class Meta:
        db_table = 'trabajador'
# --------------------------------------------------------------------
class Sueldo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    sueldo_valor_basico = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_asigfam_porcentaje = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    sueldo_asignacion_familiar = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    sueldo_bono_porcentaje = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    sueldo_monto_bono = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    sueldo_mensual = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_anual = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'sueldo'
# --------------------------------------------------------------------
class Contrato(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    id_contrato_tipo = models.ForeignKey('DropdownTipoContrato', on_delete=models.DO_NOTHING)
    id_contrato_opcion = models.ForeignKey('DropdownEmpleoTipo', on_delete=models.DO_NOTHING)
    id_empleo_tipo = models.ForeignKey('DropdownContratoOpcion', on_delete=models.DO_NOTHING)
    id_empleo_situacion = models.ForeignKey('DropdownEmpleoSituacion', on_delete=models.DO_NOTHING)
    id_empleo_area = models.ForeignKey('DropdownAreas', on_delete=models.DO_NOTHING)
    id_empleo_proyecto = models.ForeignKey('DropdownProyecto', on_delete=models.DO_NOTHING)
    id_empleo_proyecto_rol = models.ForeignKey('DropdownRolProyecto', on_delete=models.DO_NOTHING)
    empleo_departamento = models.CharField(max_length=100, null=True, blank=True)
    empleo_cargo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'contrato'
# --------------------------------------------------------------------
class DropdownRolProyecto(models.Model):
    id = models.AutoField(primary_key=True)
    rol_titulo = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_rol_proyecto'
# --------------------------------------------------------------------
class DropdownAreas(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=100)

    class Meta:
        db_table = 'dropdown_areas'
# --------------------------------------------------------------------
class DropdownTipoContrato(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_contrato = models.CharField(max_length=100)
    dleg = models.CharField(max_length=100)

    class Meta:
        db_table = 'dropdown_tipo_contrato'
# --------------------------------------------------------------------
class DropdownContratoOpcion(models.Model):
    id = models.AutoField(primary_key=True)
    opcion_contrato = models.CharField(max_length=100)

    class Meta:
        db_table = 'dropdown_contrato_opcion'
# --------------------------------------------------------------------
class DropdownEmpleoTipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_empleo = models.CharField(max_length=100)

    class Meta:
        db_table = 'dropdown_empleo_tipo'
# --------------------------------------------------------------------
class DropdownEmpleoSituacion(models.Model):
    id = models.AutoField(primary_key=True)
    situacion_empleo = models.CharField(max_length=100)

    class Meta:
        db_table = 'dropdown_empleo_situacion'
# --------------------------------------------------------------------
class DropdownProyecto(models.Model):
    id = models.AutoField(primary_key=True)
    proyecto = models.CharField(max_length=100)

    class Meta:
        db_table = 'dropdown_proyecto'
# --------------------------------------------------------------------
class CuentaBancaria(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.CharField(max_length=20)
    cuenta_bancaria_sueldo_codigo_cci = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_sueldo_codigo = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_sueldo_banco = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_codigo_cci = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_codigo = models.CharField(max_length=255, null=True, blank=True)
    cuenta_bancaria_cts_banco = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'cuenta_bancaria'
# --------------------------------------------------------------------
class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.CharField(max_length=20)
    direccion_pais = models.CharField(max_length=255, null=True, blank=True)
    direccion_departamento = models.CharField(max_length=255, null=True, blank=True)
    direccion_provincia = models.CharField(max_length=255, null=True, blank=True)
    direccion_distrito = models.CharField(max_length=255, null=True, blank=True)
    direccion_detalle = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'direccion'
# --------------------------------------------------------------------
class Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.CharField(max_length=20)
    id_estudio_nivel_educativo = models.ForeignKey('DropdownNivelEducativo', models.DO_NOTHING)
    id_estudio_situacion_especial = models.ForeignKey('DropdownSituacionesEspeciales', models.DO_NOTHING)
    id_regimen_laboral = models.ForeignKey('DropdownRegimenLaboral', models.DO_NOTHING)
    id_regimen_aseguramiento = models.ForeignKey('DropdownRegimenAseguramiento', models.DO_NOTHING)
    id_institucion = models.ForeignKey('DropdownInstituciones', models.DO_NOTHING)
    id_carrera_educativa = models.ForeignKey('DropdownCarreras', models.DO_NOTHING)
    id_estudio_capacitacion = models.ForeignKey('DropdownCapacitaciones', models.DO_NOTHING)
    id_estudio_especializacion = models.ForeignKey('DropdownEspecializaciones', models.DO_NOTHING)
    estudio_fecha_colegiatura = models.DateField(null=True, blank=True)  # Puedes ajustar este campo según tus necesidades
    id_sede_colegiatura = models.ForeignKey('DropdownSedes', models.DO_NOTHING)
    estudio_condicion = models.CharField(max_length=15, default='XXXXX')

    class Meta:
        db_table = 'estudio'
# --------------------------------------------------------------------
class DropdownNivelEducativo(models.Model):
    id = models.AutoField(primary_key=True)
    nivel_educativo = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_nivel_educativo'
# --------------------------------------------------------------------
class DropdownSituacionesEspeciales(models.Model):
    id = models.AutoField(primary_key=True)
    situacion_especial = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_situaciones_especiales'
# --------------------------------------------------------------------
class DropdownRegimenLaboral(models.Model):
    id = models.AutoField(primary_key=True)
    regimen_laboral = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_regimen_laboral'
# --------------------------------------------------------------------
class DropdownRegimenAseguramiento(models.Model):
    id = models.AutoField(primary_key=True)
    regimen_aseguramiento = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_regimen_aseguramiento'
# --------------------------------------------------------------------
class DropdownInstituciones(models.Model):
    id = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_instituciones'
# --------------------------------------------------------------------
class DropdownCarreras(models.Model):
    id = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_carreras'
# --------------------------------------------------------------------
class DropdownCapacitaciones(models.Model):
    id = models.AutoField(primary_key=True)
    capacitacion = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_capacitaciones'
# --------------------------------------------------------------------
class DropdownEspecializaciones(models.Model):
    id = models.AutoField(primary_key=True)
    especializacion = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_especializaciones'
# --------------------------------------------------------------------
class DropdownSedes(models.Model):
    id = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=255)

    class Meta:
        db_table = 'dropdown_sedes'
# --------------------------------------------------------------------
