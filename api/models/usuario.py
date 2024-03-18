# models/usuario.py
from django.db import models
from .dropdowns import DropdownRoles
from django.apps import apps

class Usuario(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    id_usuario_rol = models.ForeignKey(DropdownRoles, on_delete=models.CASCADE)
    usuario_nombres = models.CharField(max_length=100)
    usuario_apellido_paterno = models.CharField(max_length=100)
    usuario_apellido_materno = models.CharField(max_length=100)
    usuario_correo = models.EmailField(unique=True)
    usuario_contrasenia = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.usuario_apellido_paterno} {self.usuario_apellido_materno}, {self.usuario_nombres}."
