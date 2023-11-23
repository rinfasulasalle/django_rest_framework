# models/usuario.py
from django.db import models
from .dropdowns import DropdownRoles

class Usuario(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    id_usuario_rol = models.ForeignKey(DropdownRoles, on_delete=models.CASCADE)
    usuario_nombres = models.CharField(max_length=100)
    usuario_apellidos = models.CharField(max_length=100)
    usuario_correo = models.EmailField(unique=True)
    usuario_contrasenia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usuario_nombres} {self.usuario_apellidos}"
