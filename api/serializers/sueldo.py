from rest_framework import serializers
from ..models import Sueldo

class SueldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sueldo
        exclude = ['sueldo_asignacion_familiar', 'sueldo_monto_bono', 'sueldo_mensual', 'sueldo_anual']
