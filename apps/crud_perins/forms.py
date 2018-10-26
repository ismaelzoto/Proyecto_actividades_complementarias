from django import forms
from apps.crud_perins.models import periodo, inscripcion, alumnos, estado, carrera, localidad, grupo, municipio, puesto, rol, organigrama, \
    usuario, instructor, area, actividad, coordinador

#------------------------------forms Joan-------------------------------------------

class periodosForm(forms.ModelForm):
    class Meta:
        model = periodo
        fields = [
            'id_periodo',
            'nombre_corto',
            'nombre_largo',
            'fecha_inicio',
            'fecha_final',
            'status'
        ]
        labels = {
            'id_periodo' : 'Id del Periodo',
            'nombre_corto' : 'Nombre Corto',
            'nombre_largo' : 'Nombre Largo',
            'fecha_inicio' : 'Fecha de Inicio',
            'fecha_final' : 'Fecha Final',
            'status': 'Estado de periodo'
        }

        widgets = {
            'id_periodo': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_corto': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_largo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class':'datepicker'}),
            'fecha_final': forms.TextInput(attrs={'class':'datepicker'}),
            'status': forms.TextInput(attrs={'class':'form-control'}),
        }

class inscripcionForm(forms.ModelForm):
    class Meta:
        model = inscripcion
        fields = [
            'calificacion',
            'periodo',
            'actividad',
            'instructor',
            'carrera',
            'grupo',
            'area',
            'alumnos'
        ]
        labels = {
            'calificacion' : 'Calificacion',
            'periodo' : 'Nombre del periodo',
            'actividad' : 'Nombre actividad',
            'instructor' : 'Nombre instructor',
            'carrera' : 'Carrera',
            'grupo' : 'Nombre grupo',
            'area' : 'Nombre del area',
            'alumnos' : 'Nombre del alumno'
        }

        widgets = {
            'calificacion' : forms.TextInput(attrs={'class': 'form-control'}),
            'periodo' : forms.Select(attrs={'class':'form-control'}),
            'actividad' : forms.Select(attrs={'class':'form-control'}),
            'instructor' : forms.Select(attrs={'class':'form-control'}),
            'carrera' : forms.Select(attrs={'class':'form-control'}),
            'grupo' : forms.Select(attrs={'class':'form-control'}),
            'area' : forms.Select(attrs={'class':'form-control'}),
            'alumnos' : forms.Select(attrs={'class':'form-control'}),
        }

#------------------------------forms ismael-----------------------------------------

class alumnosForm(forms.ModelForm):
    class Meta:
        model = alumnos
        fields = [
            'nocontrol',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'email',
            'telefono',
            'fecha_nacimiento',
            'sexo',
            'calle',
            'numero_exterior',
            'numero_interior',
            'colonia',
            'password',
            'estatus',
            'carrera',
            'localidad',
            'rol'
        ]
        labels = {
            'nocontrol':'Numero de Control',
            'nombre':'Nombres',
            'apellido_paterno':'Apellido Paterno',
            'apellido_materno':'Apellido Materno',
            'email':'Correo Electronico',
            'telefono':'Numero de Telefono',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'sexo':'Sexo',
            'calle':'Direccion',
            'numero_exterior':'Numero Exterior',
            'numero_interior':'Numero Interior',
            'colonia':'Colonia',
            'password':'Contraseña',
            'estatus':'Estatus',
            'carrera':'Carrera',
            'localidad':'Localidad',
            'rol':'Rol'
        }

        widgets = {
            'nocontrol':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento':forms.TextInput(attrs={'class':'datepicker'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'calle':forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior':forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior':forms.TextInput(attrs={'class':'form-control'}),
            'colonia':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'estatus':forms.TextInput(attrs={'class':'form-control'}),
            'carrera':forms.Select(attrs={'class':'form-control'}),
            'localidad':forms.Select(attrs={'class':'form-control'}),
            'rol':forms.Select(attrs={'class':'form-control'})
        }

class estadoForm(forms.ModelForm):
    class Meta:
        model = estado
        fields = [
            'id_estado',
            'nombre_estado'
            ]
        labels = {
            'id_estado':'Clave de Estado',
            'nombre_estado':'Nombre del Estado'
        }
        widgets = {
            'id_estado': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_estado': forms.TextInput(attrs={'class': 'form-control'}),
        }

#-----------------------------forms javier------------------------------------------

class usuarioForm(forms.ModelForm):
    class Meta:
      model = usuario
      fields = [
          'clave',
          'nombre',
          'apellido_paterno',
          'apellido_materno',
          'organigrama',
          'password',
          'estatus',
          'rol'

      ]
      labels = {
          'clave': 'Clave',
          'nombre': 'Nombres',
          'apellido_paterno': 'Apellido Paterno',
          'apellido_materno': 'Apellido Materno',
          'organigrama': 'Organigrama',
          'password': 'Passwords',
          'estatus': 'Estatu',
          'rol':'Rol',
          'organigrama':'Organigrama'
      }

      widgets={
          'clave':forms.TextInput(attrs={'class':'form-control'}),
          'nombre':forms.TextInput(attrs={'class':'form-control'}),
          'apellido_paterno':forms.TextInput(attrs={'class':'form-control'}),
          'apellido_materno':forms.TextInput(attrs={'class':'form-control'}),
          'organigrama':forms.TextInput(attrs={'class':'datepicker'}),
          'password': forms.PasswordInput(attrs={'class': 'form-control'}),
          'estatus':forms.Select(attrs={'class':'form-control'}),
          'rol': forms.Select(attrs={'class': 'form-control'}),
          'organigrama': forms.Select(attrs={'class': 'form-control'}),
      }

class areaForm(forms.ModelForm):
    class Meta:
        model = area
        fields = [
            'id_area',
            'nombre_area'
            ]
        labels = {
            'id_area':'Clave de Area',
            'nombre_area':'Nombre del Area'
        }
        widgets = {
            'id_area': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_area': forms.TextInput(attrs={'class': 'form-control'}),
        }

#-------------------forms ivan-------------------------------

class organigramaForm(forms.ModelForm):
    class Meta:
        model= organigrama
        fields = [
            'id_organigrama',
            'area',
            'descripcion',
            'area_depende',
            'nivel',
            'tipo_area',
            'titular'
        ]
        labels = {
            'id_organigrama': 'clave organigrama',
            'area': 'Area',
            'descripcion': 'Descripcion',
            'area_depende': 'Area depende',
            'nivel': 'Nivel',
            'tipo_area': 'Tipo Area',
            'titular': 'Titular'
        }

        widgets = {
            'id_organigrama': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'area_depende': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_area': forms.TextInput(attrs={'class': 'form-control'}),
            'titular': forms.TextInput(attrs={'class': 'form-control'}),
        }

class puestoForm(forms.ModelForm):
    class Meta:
        model = puesto
        fields = [
            'id_puesto',
            'descripcion',
            'nivel',
            'tipo',
            'funciones'
        ]
        labels = {
            'id_puesto': 'Clave puesto',
            'descripcion': 'Descripcion',
            'nivel': 'Nivel',
            'tipo': 'Tipo',
            'funciones': 'Funciones'
        }
        widgets = {
            'id_puesto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'funciones': forms.TextInput(attrs={'class': 'form-control'}),
        }

#-----------------forms karyn-----------------

class grupoForm(forms.ModelForm):
    class Meta:
        model = grupo
        fields = [
            'id_grupo',
            'nombre_grupo',
            'capacidad',
            'area'
        ]
        labels = {
            'id_grupo': 'Id de grupo',
            'nombre_grupo': 'Nombre del del grupo',
            'capacidad': 'Capacidad',
            'area': 'Area'
        }

        widgets = {
            'id_grupo' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_grupo' : forms.TextInput(attrs={'class':'form-control'}),
            'capacidad' : forms.TextInput(attrs={'class':'form-control'}),
            'area' : forms.Select(attrs={'class':'form-control'})
        }

class municipioForm(forms.ModelForm):
    class Meta:
        model = municipio
        fields = [
            'id_municipio',
            'nombre_municipio',
            'estado'
        ]
        labels = {
            'id_municipio': 'Id del Municipio',
            'nombre_municipio' : 'Nombre municipio',
            'estado': 'Estado'
        }
        widgets = {
            'id_municipio': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_municipio': forms.TextInput(attrs={'class':'form-control'}),
            'estado' : forms.Select(attrs={'class':'form-control'})
        }

#-----------------------forms litzy-------------------------------

class actividadForm(forms.ModelForm):
    class Meta:
        model = actividad
        fields = [
        'nombre',
        'objetivo_general',
        'competencia',
        'temario',
        'autorizada',
        'usuario',
        'periodo',
        'instructor',
        'grupo',
        'area'
        ]
        labels = {
            'nombre': 'Nombre de la actividad',
            'objetivo_general': 'objetivo de la actividad',
            'competencia': 'competencia de la actividad',
            'temario': 'temario de la actividad',
            'autorizada':'nombre del autorizador',
            'usuario': 'nombre del usuario',
            'periodo': 'periodo de la actividad',
            'instructor': 'nombre del instructor',
            'grupo': 'nombre del grupo',
            'area': 'nombre del area'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'objetivo_general': forms.TextInput(attrs={'class': 'form-control'}),
            'competencia': forms.TextInput(attrs={'class': 'form-control'}),
            'temario': forms.TextInput(attrs={'class': 'form-control'}),
            'autorizada': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'periodo': forms.Select(attrs={'class': 'form-control'}),
            'instructor': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'})
         }

class rolForm(forms.ModelForm):
    class Meta:
        model = rol
        fields = [
            'id_rol',
            'nombre_rol',
            'descripcion'
        ]
        labels = {
            'id_rol': 'Clave rol',
            'nombre_rol': 'Nombre del rol',
            'descripcion': 'descripcion del rol'
        }
        widgets = {
               'id_rol': forms.TextInput(attrs={'class': 'form-control'}),
               'nombre_rol': forms.TextInput(attrs={'class': 'form-control'}),
               'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

           }

#----------------------form may----------------------------------

class carreraForm(forms.ModelForm):
    class Meta:
        model = carrera
        fields = [
        'clave_oficial',
        'nombre_carrera',
        'reticula',
        'nivel_escolar',
        'nombre_reducido',
        'carga_maxima',
        'creditos_totales',
        'nivel',
        'modalidad'
        ]
        labels = {
        'clave_oficial': 'Clave oficial',
        'nombre_carrera': 'Nombre de la carrera',
        'reticula': 'Reticula',
        'nivel_escolar': 'Nivel escolar',
        'nombre_reducido': 'Nombre reducido',
        'carga_maxima': 'Carga maxima',
        'creditos_totales': 'Creditos totales',
        'nivel': 'Nivel',
        'modalidad': 'Modalidad'

        }

        widgets = {
            'clave_oficial': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_carrera': forms.TextInput(attrs={'class': 'form-control'}),
            'reticula': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel_escolar': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_reducido': forms.TextInput(attrs={'class': 'form-control'}),
            'carga_maxima': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos_totales': forms.Select(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-control'}),
            'modalidad': forms.Select(attrs={'class': 'form-control'}),
         }

class localidadForm(forms.ModelForm):
    class Meta:
        model = localidad
        fields = [
        'id_localidad',
        'nombre_localidad',
        'municipio'
        ]
        labels = {
            'id_localidad': 'Clave de localidad',
            'nombre_localidad': 'Nombre de la localidad',
            'municipio': 'Municipio'
        }
        widgets = {
               'id_localidad': forms.TextInput(attrs={'class': 'form-control'}),
               'nombre_localidad': forms.TextInput(attrs={'class': 'form-control'}),
               'municipio': forms.TextInput(attrs={'class': 'form-control'}),

           }

#----------------------form nubia--------------------------------

class coordinadorForm(forms.ModelForm):
    class Meta:
        model = coordinador
        fields = [
        'usuario',
        'rol',
        'carrera',
                ]
        labels = {
        'usuario': 'Nombre de Usuario',
        'rol': 'Rol',
        'carrera': 'Carrera'
                }

        widgets = {
        'usuario': forms.Select(attrs={'class': 'form-control'}),
        'rol': forms.Select(attrs={'class': 'form-control'}),
        'carrera': forms.Select(attrs={'class': 'form-control'})
                }

class instructorForm(forms.ModelForm):
    class Meta:
        model = instructor
        fields = [
        'id_instructor',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'sexo',
        'rfc',
        'formacion'
                ]
        labels = {
        'id_instructor': 'Clave de instructor',
        'nombre': 'Nombre de instructor',
        'apellido_paterno': 'Apellido paterno',
        'apellido_materno': 'Apellido materno',
        'sexo': 'Sexo',
        'rfc': 'RFC',
        'formacion': 'Formacion'

                }
        widgets = {
        'id_instructor': forms.TextInput(attrs={'class': 'form-control'}),
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
        'sexo': forms.TextInput(attrs={'class': 'form-control'}),
        'rfc': forms.TextInput(attrs={'class': 'form-control'}),
        'formacion': forms.TextInput(attrs={'class': 'form-control'})
                }
