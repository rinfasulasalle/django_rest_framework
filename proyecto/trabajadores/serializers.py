from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id',
            'id_usuario_rol',
            'usuario_nombres',
            'usuario_apellidos',
            'usuario_correo',
            'usuario_contrasenia',
        ]