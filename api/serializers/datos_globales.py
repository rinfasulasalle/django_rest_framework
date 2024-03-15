# serializers/direccion.py
from rest_framework import serializers
from ..models import DatosGlobales

class  DatosGlobalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGlobales
        fields = '__all__'