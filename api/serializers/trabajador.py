# serializers/trabajador.py
from rest_framework import serializers
from django.utils import timezone
from ..models import Trabajador

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        #fields = '__all__'
        exclude = ['trabajador_edad', 'trabajador_record', 'trabajador_total_anios_exp']
    def create(self, validated_data):
        # Establecer automáticamente la fecha de ingreso al sistema
        validated_data['trabajador_fecha_ingreso_sistema'] = timezone.now().date()
        return super().create(validated_data)
