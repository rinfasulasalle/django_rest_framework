# models/trabajador.py
from django.db import models
from .usuario import Usuario

class Trabajador(models.Model):
    #usuario_id = models.CharField(max_length=20, primary_key=True)
    trabajador_tipo_documento = models.CharField(max_length=100)
    trabajador_path_documento = models.CharField(max_length=255, default='PATH/noNe')
    trabajador_nacionalidad = models.CharField(max_length=100, default='No Especificado')
    trabajador_fecha_nacimiento = models.DateField()
    trabajador_ubigeo = models.CharField(max_length=255, default='No Especificado')
    trabajador_telefono = models.CharField(max_length=100)
    trabajador_sexo = models.CharField(
        max_length=15,
        choices=[
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('No Especificado', 'No Especificado'),
        ],
        default='No Especificado'
    )
    trabajador_estado_civil = models.CharField(
        max_length=15,
        choices=[
            ('Soltero', 'Soltero'),
            ('Casado', 'Casado'),
            ('Viudo', 'Viudo'),
            ('Divorciado', 'Divorciado'),
            ('Conviviente', 'Conviviente'),
            ('No Especificado', 'No Especificado'),
        ],
        default='No Especificado'
    )
    trabajador_path_doc_estado_civil = models.CharField(max_length=255, default='PATH/noNe')
    trabajador_fecha_ingreso_sistema = models.DateField()
    trabajador_fecha_ingreso = models.DateField()
    trabajador_edad = models.IntegerField()
    trabajador_record = models.DecimalField(max_digits=20, decimal_places=2)
    trabajador_exp_previa = models.DecimalField(max_digits=20, decimal_places=2)
    trabajador_total_anios_exp = models.DecimalField(max_digits=20, decimal_places=2)

    # Cambia el nombre del campo a algo diferente a 'usuario'
    usuario_relacionado = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Trabajador: {self.usuario_relacionado}, {self.usuario_relacionado.usuario_nombres} {self.usuario_relacionado.usuario_apellidos}"
