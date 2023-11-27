from rest_framework import viewsets
from .models import (
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
    Usuario,
    Trabajador,
    Contrato,
    CuentaBancaria,
    Direccion,
    Estudio,
)
from .serializers import (
    DropdownRolesSerializer,
    DropdownRolProyectoSerializer,
    DropdownAreasSerializer,
    DropdownTipoContratoSerializer,
    DropdownContratoOpcionSerializer,
    DropdownEmpleoTipoSerializer,
    DropdownEmpleoSituacionSerializer,
    DropdownProyectoSerializer,
    DropdownNivelEducativoSerializer,
    DropdownSituacionesEspecialesSerializer,
    DropdownRegimenLaboralSerializer,
    DropdownRegimenAseguramientoSerializer,
    DropdownInstitucionesSerializer,
    DropdownCarrerasSerializer,
    DropdownCapacitacionesSerializer,
    DropdownEspecializacionesSerializer,
    DropdownSedesSerializer,
    UsuarioSerializer,
    TrabajadorSerializer,
    ContratoSerializer,
    CuentaBancariaSerializer,
    DireccionSerializer,
    EstudioSerializer,
)

# Vistas basadas en conjuntos (viewsets) para modelos de "dropdowns"
class DropdownRolesViewSet(viewsets.ModelViewSet):
    queryset = DropdownRoles.objects.all()
    serializer_class = DropdownRolesSerializer

class DropdownRolProyectoViewSet(viewsets.ModelViewSet):
    queryset = DropdownRolProyecto.objects.all()
    serializer_class = DropdownRolProyectoSerializer

class DropdownAreasViewSet(viewsets.ModelViewSet):
    queryset = DropdownAreas.objects.all()
    serializer_class = DropdownAreasSerializer

class DropdownTipoContratoViewSet(viewsets.ModelViewSet):
    queryset = DropdownTipoContrato.objects.all()
    serializer_class = DropdownTipoContratoSerializer

class DropdownContratoOpcionViewSet(viewsets.ModelViewSet):
    queryset = DropdownContratoOpcion.objects.all()
    serializer_class = DropdownContratoOpcionSerializer

class DropdownEmpleoTipoViewSet(viewsets.ModelViewSet):
    queryset = DropdownEmpleoTipo.objects.all()
    serializer_class = DropdownEmpleoTipoSerializer

class DropdownEmpleoSituacionViewSet(viewsets.ModelViewSet):
    queryset = DropdownEmpleoSituacion.objects.all()
    serializer_class = DropdownEmpleoSituacionSerializer

class DropdownProyectoViewSet(viewsets.ModelViewSet):
    queryset = DropdownProyecto.objects.all()
    serializer_class = DropdownProyectoSerializer

class DropdownNivelEducativoViewSet(viewsets.ModelViewSet):
    queryset = DropdownNivelEducativo.objects.all()
    serializer_class = DropdownNivelEducativoSerializer

class DropdownSituacionesEspecialesViewSet(viewsets.ModelViewSet):
    queryset = DropdownSituacionesEspeciales.objects.all()
    serializer_class = DropdownSituacionesEspecialesSerializer

class DropdownRegimenLaboralViewSet(viewsets.ModelViewSet):
    queryset = DropdownRegimenLaboral.objects.all()
    serializer_class = DropdownRegimenLaboralSerializer

class DropdownRegimenAseguramientoViewSet(viewsets.ModelViewSet):
    queryset = DropdownRegimenAseguramiento.objects.all()
    serializer_class = DropdownRegimenAseguramientoSerializer

class DropdownInstitucionesViewSet(viewsets.ModelViewSet):
    queryset = DropdownInstituciones.objects.all()
    serializer_class = DropdownInstitucionesSerializer

class DropdownCarrerasViewSet(viewsets.ModelViewSet):
    queryset = DropdownCarreras.objects.all()
    serializer_class = DropdownCarrerasSerializer

class DropdownCapacitacionesViewSet(viewsets.ModelViewSet):
    queryset = DropdownCapacitaciones.objects.all()
    serializer_class = DropdownCapacitacionesSerializer

class DropdownEspecializacionesViewSet(viewsets.ModelViewSet):
    queryset = DropdownEspecializaciones.objects.all()
    serializer_class = DropdownEspecializacionesSerializer

class DropdownSedesViewSet(viewsets.ModelViewSet):
    queryset = DropdownSedes.objects.all()
    serializer_class = DropdownSedesSerializer

# ... Puede agregar más viewsets de "dropdowns" según sea necesario

# Vistas basadas en conjuntos (viewsets) para modelos principales
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class CuentaBancariaViewSet(viewsets.ModelViewSet):
    queryset = CuentaBancaria.objects.all()
    serializer_class = CuentaBancariaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class EstudioViewSet(viewsets.ModelViewSet):
    queryset = Estudio.objects.all()
    serializer_class = EstudioSerializer

# ... Puede agregar más viewsets para modelos principales según sea necesario
