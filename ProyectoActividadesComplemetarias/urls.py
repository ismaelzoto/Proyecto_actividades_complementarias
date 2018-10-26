from django.conf.urls import url, include

urlpatterns = [
    url(r'^periodos/', include(('apps.crud_perins.urls', 'apps'), namespace='periodos')),
    url(r'^inscripciones/', include(('apps.crud_perins.urls', 'apps'), namespace='inscripciones')),

#--------------------url ismael----------------------------------------------------
    url(r'^alumnos/', include(('apps.crud_perins.urls', 'apps'), namespace='alumnos')),
    url(r'^estados/', include(('apps.crud_perins.urls', 'apps'), namespace='estados')),

#--------------------url javier----------------------------------------------------
    url(r'^usuario/', include(('apps.crud_perins.urls','apps'), namespace='usuario')),
    url(r'^area/',include(('apps.crud_perins.urls','apps'), namespace='area')),

#------------------------------url ivan-------------------
    url(r'^organigramas/', include(('apps.crud_perins.urls', 'apps'), namespace='organigramas')),
    url(r'^puestos/', include(('apps.crud_perins.urls', 'apps'), namespace='puestos')),

#-----------------url karyn-------------------------------
    url(r'^grupos/', include(('apps.crud_perins.urls', 'apps'), namespace='grupos')),
    url(r'^municipios/', include(('apps.crud_perins.urls', 'apps'), namespace='municipios')),

#----------------url litzy-----------------------------------
    url(r'^actividades/', include(('apps.crud_perins.urls', 'apps'), namespace='actividades')),
    url(r'^roles/', include(('apps.crud_perins.urls', 'apps'), namespace='roles')),

#---------------url may---------------------------------------
    url(r'^carrera/', include(('apps.crud_perins.urls', 'apps'), namespace='carrera')),
    url(r'^localidad/', include(('apps.crud_perins.urls', 'apps'), namespace='localidad')),

#---------------url nubia--------------------------------------
    url(r'^coordinadores/', include(('apps.crud_perins.urls', 'apps'), namespace='coordinadores')),
    url(r'^instructores/', include(('apps.crud_perins.urls', 'apps'), namespace='instructores'))

]
