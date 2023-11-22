from .models import Usuario
from rest_framework import viewsets
from rest_framework import permissions
from proyecto.trabajadores.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
