import django_filters
from apps.crud_perins.models import periodo, inscripcion, alumnos, estado, carrera, localidad, grupo, municipio, puesto, rol, organigrama, \
    usuario, instructor, area, actividad, coordinador

class periodoFilter(django_filters.FilterSet):
    class Meta:
        model = periodo
        fields = ['id_periodo']

class inscripFilter(django_filters.FilterSet):
    class Meta:
        model = inscripcion
        fields = ['calificacion']

#----------------------filters ismael---------------------------

class alumnosFilter(django_filters.FilterSet):
    class Meta:
        model = alumnos
        fields = ['nocontrol', 'nombre', 'carrera']

class estadoFilter(django_filters.FilterSet):
    class Meta:
        model = estado
        fields = ['nombre_estado']

#-------------------------------filters javier-----------------------------
class usuarioFilter(django_filters.FilterSet):
    class Meta:
        model = usuario
        fields = ['clave','nombre']

class areaFilter(django_filters.FilterSet):
    class Meta:
        model = area
        fields = ['id_area', 'nombre_area' ]

#---------filters ivan----------------------
class organigramaFilter(django_filters.FilterSet):
    class Meta:
        model = organigrama
        fields = ['id_organigrama', 'area', 'nivel']

class puestoFilter(django_filters.FilterSet):
    class Meta:
        model = puesto
        fields = ['id_puesto', 'nivel']

#-------------------filters karyn-----
class grupoFilter(django_filters.FilterSet):
    class Meta:
        model = grupo
        fields = ['id_grupo']

class municipioFilter(django_filters.FilterSet):
    class Meta:
        model = municipio
        fields = ['id_municipio']

#---------------------filters litzy------------
class actividadFilter(django_filters.FilterSet):
    class Meta:
        model = actividad
        fields = ['nombre', 'area']

class rolFilter(django_filters.FilterSet):
    class Meta:
        model = rol
        fields = ['id_rol', 'nombre_rol']

#------------------filters may---------------------
class carreraFilter(django_filters.FilterSet):
    class Meta:
        model = carrera
        fields = ['clave_oficial', 'nombre_carrera']



class localidadFilter(django_filters.FilterSet):
    class Meta:
        model = localidad
        fields = ['id_localidad', 'nombre_localidad']