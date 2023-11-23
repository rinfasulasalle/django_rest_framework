# mi_proyecto/mi_aplicacion/serializers/usuario_serializer.py
from rest_framework import serializers
from ..models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
