# serializers/__init__.py
from .dropdowns import (
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
    # ... otros serializadores de dropdowns
)
from .usuario import UsuarioSerializer
from .trabajador import TrabajadorSerializer
from .contrato import ContratoSerializer
from .cuenta_bancaria import CuentaBancariaSerializer
from .direccion import DireccionSerializer
from .estudio import EstudioSerializer
# ... otros serializadores para modelos principales si los tienes
