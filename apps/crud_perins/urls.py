from django.conf.urls import url
from apps.crud_perins.views import periodoCreate, periodoList, periodoDelete, periodoUpdate, periodoShow, search, \
    inscripCreate, inscripList, inscripDelete, inscripUpdate, inscripShow, searchT

from apps.crud_perins.views import alumnosCreate, alumnosList, alumnosDelete, alumnosUpdate, alumnoShow, searchI, \
    estadoCreate,estadoDelete,estadoList,estadoShow,estadoUpdate, search_I

from apps.crud_perins.views import usuarioCreate, usuarioList, usuarioDelete, usuarioUpdate, usuarioShow, searchJ, \
    areaCreate,areaList,areaDelete,areaUpdate,areaShow, search_J

from apps.crud_perins.views import organigramaCreate, organigramaList, organigrmaDelete, organigramaUpdate, organigramaShow, searchV, \
    puestoCreate, puestoList, puestoDelete, puestoUpdate, puestoShow, search_V

from apps.crud_perins.views import grupoCreate, grupoList, grupoDelete, grupoUpdate, grupoShow, gruposearch, \
    muniCreate, muniList, muniDelete, muniUpdate, muniShow, munisearch

from apps.crud_perins.views import actividadCreate, actividadList, actividadDelete, actividadUpdate, actividadShow, \
    rolCreate, rolList, rolDelete, rolUpdate, rolShow, searchL, search_L

from apps.crud_perins.views import carreraCreate, carreraList, carreraDelete, carreraUpdate, carreraShow, searchM, \
    localidadCreate, localidadList, localidadDelete, localidadShow, localidadUpdate, buscarM
urlpatterns = [
#-----------------------------tablas de joan-------------------------------------------
    url(r'^nuevo/', periodoCreate.as_view(), name='periodo_crear'),
    url(r'^listar/', periodoList.as_view(), name='periodos_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', periodoDelete.as_view(), name='periodo_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', periodoUpdate.as_view(), name='periodo_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', periodoShow.as_view(), name='periodo_mostrar'),
    url(r'^buscar/$', search, name='periodo_buscar'),

    url(r'^Nuevo/', inscripCreate.as_view(), name='inscrip_Crear'),
    url(r'^Listar/', inscripList.as_view(), name='inscrips_Listar'),
    url(r'^Eliminar/(?P<pk>\d+)/$', inscripDelete.as_view(), name='inscrip_Eliminar'),
    url(r'^Editar/(?P<pk>\d+)/$', inscripUpdate.as_view(), name='inscrip_Editar'),
    url(r'^Mostrar/(?P<pk>\d+)/$', inscripShow.as_view(), name='inscrip_Mostrar'),
    url(r'^Buscar/$', searchT, name='inscrip_Buscar'),
#--------------------------Tablas de Ismael--------------------------------------------
    url(r'^nuevoI/', alumnosCreate.as_view(), name='alumno_crear'),
    url(r'^listarI/', alumnosList.as_view(), name='alumnos_listar'),
    url(r'^eliminarI/(?P<pk>\d+)/$', alumnosDelete.as_view(), name='alumno_eliminar'),
    url(r'^modificarI/(?P<pk>\d+)/$', alumnosUpdate.as_view(), name='alumno_editar'),
    url(r'^mostrarI/(?P<pk>\d+)/$', alumnoShow.as_view(), name='alumno_mostrar'),
    url(r'^buscarI/$', searchI, name='alumno_buscar'),
    #aqui inician las urls de estado
    url(r'^nuevo_e/', estadoCreate.as_view(), name='estado_crea'),
    url(r'^listar_e/', estadoList.as_view(), name='estado_lista'),
    url(r'^editar_e/(?P<pk>\d+)/$', estadoUpdate.as_view(), name='estado_edita'),
    url(r'^borrar_e/(?P<pk>\d+)/$', estadoDelete.as_view(), name='estado_borrar'),
    url(r'^ver_e/(?P<pk>\d+)/$', estadoShow.as_view(), name='estado_ver'),
    url(r'^buscar_e/$', search_I, name='estado_busca'),
#----------------------url javier-----------------------------------------------------
    url(r'^nuevoJ/', usuarioCreate.as_view(), name='usuario_crear'),
    url(r'^listarJ/', usuarioList.as_view(), name='usuario_listar'),
    url(r'^eliminarJ/(?P<pk>\d+)/$', usuarioDelete.as_view(), name='usuario_eliminar'),
    url(r'^editarJ/(?P<pk>\d+)/$', usuarioUpdate.as_view(), name='usuario_editar'),
    url(r'^mostrarJ/(?P<pk>\d+)/$', usuarioShow.as_view(), name='usuario_mostrar'),
    url(r'^buscarJ/$', searchJ, name='usuario_buscar'),

    url(r'^nuevos_J/', areaCreate.as_view(), name='area_crea'),
    url(r'^lista_J/', areaList.as_view(), name='area_lista'),
    url(r'^elimina_J/(?P<pk>\d+)/$', areaDelete.as_view(), name='area_elimina'),
    url(r'^edita_J/(?P<pk>\d+)/$', areaUpdate.as_view(), name='area_edita'),
    url(r'^muestra_J/(?P<pk>\d+)/$', areaShow.as_view(), name='area_muestra'),
    url(r'^buscador_J/$', search_J, name='area_busca'),

#------------------------url de ivan--------------------------------
    url(r'^nuevoV/', organigramaCreate.as_view(), name='organigrama_crear'),
    url(r'^listarV/', organigramaList.as_view(), name='organigrama_listar'),
    url(r'^eliminarV/(?P<pk>\d+)/$', organigrmaDelete.as_view(), name='organigrama_eliminar'),
    url(r'^modificarV/(?P<pk>\d+)/$', organigramaUpdate.as_view(), name='organigrama_editar'),
    url(r'^mostrarV/(?P<pk>\d+)/$', organigramaShow.as_view(), name='organigrama_mostrar'),
    url(r'^buscarV/', searchV, name='organigrama_buscar'),

    url(r'^nuevos_V/', puestoCreate.as_view(), name='puesto_crear'),
    url(r'^listarr_V/', puestoList.as_view(), name='puesto_listar'),
    url(r'^eliminarr_V/(?P<pk>\d+)/$', puestoDelete.as_view(), name='puesto_eliminar'),
    url(r'^modificarr_V/(?P<pk>\d+)/$', puestoUpdate.as_view(), name='puesto_editar'),
    url(r'^mostrarr_V/(?P<pk>\d+)/$', puestoShow.as_view(), name='puesto_mostrar'),
    url(r'^search_V/$', search_V, name='puesto_search'),

#-------------------------url karyn-----------------------------------------
    url(r'^nuevok/', grupoCreate.as_view(), name='grupo_crear'),
    url(r'^listark/', grupoList.as_view(), name='grupo_listar'),
    url(r'^eliminark/(?P<pk>\d+)/$', grupoDelete.as_view(), name='grupo_eliminar'),
    url(r'^editark/(?P<pk>\d+)/$', grupoUpdate.as_view(), name='grupo_editar'),
    url(r'^mostrark/(?P<pk>\d+)/$', grupoShow.as_view(), name='grupo_mostrar'),
    url(r'^buscark/$', gruposearch, name='grupo_buscar'),

    url(r'^Nuevo_k/', muniCreate.as_view(), name='muni_crear'),
    url(r'^Listar_k/', muniList.as_view(), name='muni_listar'),
    url(r'^Eliminar_k/(?P<pk>\d+)/$', muniDelete.as_view(), name='muni_eliminar'),
    url(r'^Editar_k/(?P<pk>\d+)/$', muniUpdate.as_view(), name='muni_editar'),
    url(r'^Mostrar_k/(?P<pk>\d+)/$', muniShow.as_view(), name='muni_mostrar'),
    url(r'^Buscar_k/$', munisearch, name='muni_buscar'),

#--------------------url litzy---------------------------------------------
    url(r'^nuevoL/', actividadCreate.as_view(), name='actividad_crear'),
    url(r'^listarL/', actividadList.as_view(), name='actividad_listar'),
    url(r'^eliminarL/(?P<pk>\d+)/$', actividadDelete.as_view(), name='actividad_eliminar'),
    url(r'^modificarL/(?P<pk>\d+)/$', actividadUpdate.as_view(), name='actividad_editar'),
    url(r'^mostrarL/(?P<pk>\d+)/$', actividadShow.as_view(), name='actividad_mostrar'),
    url(r'^buscarL/', searchL, name='actividad_buscar'),

    url(r'^nuevos_L/', rolCreate.as_view(), name='rol_crear'),
    url(r'^listarr_L/', rolList.as_view(), name='rol_listar'),
    url(r'^eliminarr_L/(?P<pk>\d+)/$', rolDelete.as_view(), name='rol_eliminar'),
    url(r'^modificarr_L/(?P<pk>\d+)/$', rolUpdate.as_view(), name='rol_editar'),
    url(r'^mostrarr_L/(?P<pk>\d+)/$', rolShow.as_view(), name='rol_mostrar'),
    url(r'^search_L/$', search_L, name='rol_search'),

#--------------------url may----------------------------
    url(r'^nuevoM/', carreraCreate.as_view(), name='carrera_crear'),
    url(r'^listarM/', carreraList.as_view(), name='carrera_listar'),
    url(r'^eliminarM/(?P<pk>\d+)/$', carreraDelete.as_view(), name='carrera_eliminar'),
    url(r'^modificarM/(?P<pk>\d+)/$', carreraUpdate.as_view(), name='carrera_editar'),
    url(r'^mostrarM/(?P<pk>\d+)/$', carreraShow.as_view(), name='carrera_mostrar'),
    url(r'^searchM/$', searchM, name='carrera_buscar'),

    url(r'^nuevosM/', localidadCreate.as_view(), name='localidad_crear'),
    url(r'^listasM/', localidadList.as_view(), name='localidad_listar'),
    url(r'^eliminasM/(?P<pk>\d+)/$', localidadDelete.as_view(), name='localidad_eliminar'),
    url(r'^modificasM/(?P<pk>\d+)/$', localidadUpdate.as_view(), name='localidad_editar'),
    url(r'^muestrasM/(?P<pk>\d+)/$', localidadShow.as_view(), name='localidad_mostrar'),
    url(r'^buscasM/$', buscarM, name='localidad_buscar'),
]
