# models/trabajador.py
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime
from .usuario import Usuario

class Trabajador(models.Model):
    usuario_relacionado = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    trabajador_tipo_documento = models.CharField(max_length=100)
    #trabajador_path_documento = models.CharField(max_length=255, default='PATH/noNe')
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
    #trabajador_path_doc_estado_civil = models.CharField(max_length=255, default='PATH/noNe')
    trabajador_fecha_ingreso = models.DateField()
    trabajador_fecha_ingreso_sistema = models.DateField(auto_now_add=True)
    trabajador_edad = models.IntegerField(blank=True, null=True)  # Se calcula automáticamente
    trabajador_record = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)  # Se calculará automáticamente
    trabajador_exp_previa = models.DecimalField(max_digits=20, decimal_places=2)
    trabajador_total_anios_exp = models.DecimalField(max_digits=20, decimal_places=2)
    activo = models.BooleanField(default=True)
    # --------------------------------------------------------
    def calcular_edad(self):
        if self.trabajador_fecha_nacimiento:
            today = timezone.now().date()
            born = self.trabajador_fecha_nacimiento
            self.trabajador_edad = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    def calcular_record(self):
        if self.trabajador_fecha_ingreso:
            hoy = timezone.now().date()
            fecha_ingreso = self.trabajador_fecha_ingreso
            dias_trabajados = (hoy - fecha_ingreso).days
            self.trabajador_record = dias_trabajados / 365.25
    def calcular_total_exp(self):
        if self.trabajador_exp_previa:
            total_exp = self.trabajador_exp_previa
            if self.trabajador_record:
                total_exp += self.trabajador_record
            self.trabajador_total_anios_exp = total_exp

    def __str__(self):
        return f"Trabajador: {self.usuario_relacionado}, {self.usuario_relacionado.usuario_nombres} {self.usuario_relacionado.usuario_apellidos}"
# Señal para calcular campos antes de guardar
@receiver(pre_save, sender=Trabajador)
def actualizar_campos(sender, instance, **kwargs):
    instance.calcular_edad()
    instance.calcular_record()
    instance.calcular_total_exp()