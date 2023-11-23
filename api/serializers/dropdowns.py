# dropdowns_serializer.py
from rest_framework import serializers
from ..models import (
    DropdownRoles,
    DropdownRolProyecto,
    DropdownAreas,
    DropdownTipoContrato,
    DropdownContratoOpcion,
    DropdownEmpleoTipo,
    DropdownEmpleoSituacion,
    DropdownProyecto,
    DropdownNivelEducativo,
    DropdownSituacionesEspeciales,
    DropdownRegimenLaboral,
    DropdownRegimenAseguramiento,
    DropdownInstituciones,
    DropdownCarreras,
    DropdownCapacitaciones,
    DropdownEspecializaciones,
    DropdownSedes,
)

class DropdownRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownRoles
        fields = '__all__'

class DropdownRolProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownRolProyecto
        fields = '__all__'

class DropdownAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownAreas
        fields = '__all__'

class DropdownTipoContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownTipoContrato
        fields = '__all__'

class DropdownContratoOpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownContratoOpcion
        fields = '__all__'

class DropdownEmpleoTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownEmpleoTipo
        fields = '__all__'

class DropdownEmpleoSituacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownEmpleoSituacion
        fields = '__all__'

class DropdownProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownProyecto
        fields = '__all__'

class DropdownNivelEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownNivelEducativo
        fields = '__all__'

class DropdownSituacionesEspecialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownSituacionesEspeciales
        fields = '__all__'

class DropdownRegimenLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownRegimenLaboral
        fields = '__all__'

class DropdownRegimenAseguramientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownRegimenAseguramiento
        fields = '__all__'

class DropdownInstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownInstituciones
        fields = '__all__'

class DropdownCarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownCarreras
        fields = '__all__'

class DropdownCapacitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownCapacitaciones
        fields = '__all__'

class DropdownEspecializacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownEspecializaciones
        fields = '__all__'

class DropdownSedesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownSedes
        fields = '__all__'
