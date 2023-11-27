from django.urls import path, include
from rest_framework import routers
from .views import (
    DropdownRolesViewSet,
    DropdownRolProyectoViewSet,
    DropdownAreasViewSet,
    DropdownTipoContratoViewSet,
    DropdownContratoOpcionViewSet,
    DropdownEmpleoTipoViewSet,
    DropdownEmpleoSituacionViewSet,
    DropdownProyectoViewSet,
    DropdownNivelEducativoViewSet,
    DropdownSituacionesEspecialesViewSet,
    DropdownRegimenLaboralViewSet,
    DropdownRegimenAseguramientoViewSet,
    DropdownInstitucionesViewSet,
    DropdownCarrerasViewSet,
    DropdownCapacitacionesViewSet,
    DropdownEspecializacionesViewSet,
    DropdownSedesViewSet,
    UsuarioViewSet,
    TrabajadorViewSet,
    ContratoViewSet,
    CuentaBancariaViewSet,
    DireccionViewSet,
    EstudioViewSet,
)


router = routers.DefaultRouter()

# Rutas para modelos de "dropdowns"
router.register(r'dropdown_roles', DropdownRolesViewSet)
router.register(r'dropdown_rol_proyecto', DropdownRolProyectoViewSet)
router.register(r'dropdown_areas', DropdownAreasViewSet)
router.register(r'dropdown_tipo_contrato', DropdownTipoContratoViewSet)
router.register(r'dropdown_contrato_opcion', DropdownContratoOpcionViewSet)
router.register(r'dropdown_empleo_tipo', DropdownEmpleoTipoViewSet)
router.register(r'dropdown_empleo_situacion', DropdownEmpleoSituacionViewSet)
router.register(r'dropdown_proyecto', DropdownProyectoViewSet)
router.register(r'dropdown_nivel_educativo', DropdownNivelEducativoViewSet)
router.register(r'dropdown_situaciones_especiales', DropdownSituacionesEspecialesViewSet)
router.register(r'dropdown_regimen_laboral', DropdownRegimenLaboralViewSet)
router.register(r'dropdown_regimen_aseguramiento', DropdownRegimenAseguramientoViewSet)
router.register(r'dropdown_instituciones', DropdownInstitucionesViewSet)
router.register(r'dropdown_carreras', DropdownCarrerasViewSet)
router.register(r'dropdown_capacitaciones', DropdownCapacitacionesViewSet)
router.register(r'dropdown_especializaciones', DropdownEspecializacionesViewSet)
router.register(r'dropdown_sedes', DropdownSedesViewSet)

# Rutas para modelos principales
router.register(r'usuario', UsuarioViewSet)
router.register(r'trabajador', TrabajadorViewSet)
router.register(r'contrato', ContratoViewSet)
router.register(r'cuenta_bancaria', CuentaBancariaViewSet)
router.register(r'direccion', DireccionViewSet)
router.register(r'estudio', EstudioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]