from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.crud_perins.models import inscripcion, periodo, alumnos, estado, carrera, localidad, grupo, municipio, puesto, rol,\
organigrama, usuario, instructor, area, actividad, coordinador
from apps.crud_perins.forms import periodosForm, inscripcionForm, alumnosForm, estadoForm, usuarioForm, areaForm, organigramaForm, \
    puestoForm, grupoForm, municipioForm, actividadForm, rolForm, carreraForm, localidadForm, instructorForm, coordinadorForm
from apps.crud_perins.filters import periodoFilter, inscripFilter, alumnosFilter, estadoFilter, usuarioFilter, areaFilter, \
    organigramaFilter, puestoFilter, grupoFilter, municipioFilter, actividadFilter, rolFilter, carreraFilter, localidadFilter, \
    coordinadorFilter, instructorFilter
from django.urls import reverse_lazy


#-------------------------------------------view joan--------------------------------
class periodoCreate(CreateView):
    model = periodo
    form_class = periodosForm
    template_name = 'crudperins/periodo_form.html'
    success_url = reverse_lazy('periodos:periodo_crear')
class periodoList(ListView):
    queryset = periodo.objects.order_by('id_periodo')
    template_name = 'crudperins/periodo_list.html'
    paginate_by = 10
class periodoUpdate(UpdateView):
    model = periodo
    form_class = periodosForm
    template_name = 'crudperins/periodo_form.html'
    success_url = reverse_lazy('periodos:periodos_listar')
class periodoDelete(DeleteView):
    model = periodo
    template_name = 'crudperins/periodo_delete.html'
    success_url = reverse_lazy('periodos:periodos_listar')
class periodoShow(DetailView):
    model = periodo
    template_name = 'crudperins/periodo_show.html'
def search(request):
    periodo_list = periodo.objects.all()
    periodo_filter = periodoFilter(request.GET, queryset=periodo_list)
    return render(request, 'crudperins/periodo_list_filter.html', {'filter': periodo_filter})
#inicia inscripciones
class inscripCreate(CreateView):
    model = inscripcion
    form_class = inscripcionForm
    template_name = 'crudperins/inscrip_form.html'
    success_url = reverse_lazy('inscripciones:inscrip_Crear')
class inscripList(ListView):
    queryset = inscripcion.objects.order_by('calificacion')
    template_name = 'crudperins/inscrip_list.html'
    paginate_by = 10
class inscripUpdate(UpdateView):
    model = inscripcion
    form_class = inscripcionForm
    template_name = 'crudperins/inscrip_form.html'
    success_url = reverse_lazy('periodos:inscrips_Listar')
class inscripDelete(DeleteView):
    model = inscripcion
    template_name = 'crudperins/inscrip_delete.html'
    success_url = reverse_lazy('inscripciones:inscrips_Listar')
class inscripShow(DetailView):
    model = inscripcion
    template_name = 'crudperins/inscrip_show.html'
def searchT(request):
    inscrip_list = inscripcion.objects.all()
    inscrip_filter = inscripFilter(request.GET, queryset=inscrip_list)
    return render(request, 'crudperins/inscrip_list_filter.html', {'filter': inscrip_filter})


#-------------------------------------------view ismael--------------------------------
class alumnosCreate(CreateView):
    model = alumnos
    form_class = alumnosForm
    template_name = 'crudperins/alumnos_form.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')
class alumnosList(ListView):
    queryset = alumnos.objects.order_by('nocontrol')
    template_name = 'crudperins/alumnos_list.html'
    paginate_by = 5
class alumnosUpdate(UpdateView):
    model = alumnos
    form_class = alumnosForm
    template_name = 'crudperins/alumnos_form.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')
class alumnosDelete(DeleteView):
    model = alumnos
    template_name = 'crudperins/alumnos_delete.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')
class alumnoShow(DetailView):
    model = alumnos
    template_name = 'crudperins/alumno_show.html'
def searchI(request):
    alumnos_list = alumnos.objects.all()
    alumnos_filter = alumnosFilter(request.GET, queryset=alumnos_list)
    return render(request, 'crudperins/alumnos_list_filter.html', {'filter': alumnos_filter})
#aqui inicia la vista de estado
class estadoCreate(CreateView):
    model = estado
    form_class = estadoForm
    template_name = 'crudperins/estados_form.html'
    success_url = reverse_lazy('estados:estado_lista')
class estadoList(ListView):
    queryset = estado.objects.order_by('id_estado')
    template_name = 'crudperins/estados_list.html'
    paginate_by = 10
class estadoUpdate(UpdateView):
    model = estado
    form_class = estadoForm
    template_name = 'crudperins/estados_form.html'
    success_url = reverse_lazy('estados:estado_lista')
class estadoDelete(DeleteView):
    model = estado
    template_name = 'crudperins/estados_delete.html'
    success_url = reverse_lazy('estados:estado_lista')
class estadoShow(DetailView):
    model = estado
    template_name = 'crudperins/estado_show.html'
def search_I(request):
    estado_list = estado.objects.all()
    estado_filter = estadoFilter(request.GET, queryset=estado_list)
    return render(request, 'crudperins/estados_list_filter.html', {'filter': estado_filter})


#------------------------------------view javier------------------------------------
class usuarioCreate(CreateView):
    model = usuario
    form_class = usuarioForm
    template_name = 'crudperins/usuario_form.html'
    success_url = reverse_lazy('usuarios:usuario_listar')
class usuarioList(ListView):
    queryset = usuario.objects.order_by('clave')
    template_name = 'crudperins/usuario_list.html'
    paginate_by = 10
class usuarioUpdate(UpdateView):
    model = usuario
    form_class = usuarioForm
    template_name = 'crudperins/usuario_form.html'
    success_url = reverse_lazy('usuarios:usuario_listar')
class usuarioDelete(DeleteView):
    model = usuario
    template_name = 'crudperins/usuario_delete.html'
    success_url = reverse_lazy('usuarios:usuario_listar')
class usuarioShow(DetailView):
    model = usuario
    template_name = 'crudperins/usuario_show.html'
def searchJ(request):
    usuario_list = usuario.objects.all()
    usuario_filter = usuarioFilter(request.GET, queryset=usuario_list)
    return  render(request, 'crudperins/usuario_list_filter.html',{'filter':usuario_filter})
#aqui iniicia area
class areaCreate(CreateView):
    model = area
    form_class = areaForm
    template_name = 'crudperins/area_form.html'
    success_url = reverse_lazy('area:area_lista')
class areaList(ListView):
    queryset = area.objects.order_by('id_area')
    template_name = 'crudperins/area_list.html'
    paginate_by = 10
class areaUpdate(UpdateView):
    model = area
    form_class = areaForm
    template_name = 'crudperins/area_form.html'
    success_url = reverse_lazy('area:area_lista')
class areaDelete(DeleteView):
    model = area
    template_name = 'crudperins/area_delete.html'
    success_url = reverse_lazy('area:area_lista')
class areaShow(DetailView):
    model = area
    template_name = 'crudperins/usuario_show.html'
def search_J(request):
    area_list = area.objects.all()
    area_filter = areaFilter(request.GET, queryset=area_list)
    return  render(request, 'crudperins/usuario_list_filter.html',{'filter':area_filter})


#--------------view de ivan-----------------------
class organigramaCreate(CreateView):
    model = organigrama
    form_class = organigramaForm
    template_name = 'crudperins/organigrama_form.html'
    success_url = reverse_lazy('organigramas:organigrama_listar')
class organigramaList(ListView):
    queryset = organigrama.objects.order_by('id_organigrama')
    template_name = 'crudperins/organigrama_list.html'
class organigramaUpdate(UpdateView):
    model = organigrama
    form_class = organigramaForm
    template_name = 'crudperins/organigrama_form.html'
    success_url = reverse_lazy('organigramas:organigrama_listar')
class organigrmaDelete(DeleteView):
    model = organigrama
    template_name = 'crudperins/organigrama_delete.html'
    success_url = reverse_lazy('organigramas:organigrama_listar')
class organigramaShow(DeleteView):
    model = organigrama
    template_name = 'crudperins/organigrama_show.html'
def searchV(request):
    organigrama_list = organigrama.objects.all()
    organigrama_filter = organigramaFilter(request.GET, queryset=organigrama_list)
    return render(request, 'crudperins/organigramas_list_filter.html', {'filter': organigrama_filter})
#inicia puesto
class puestoCreate(CreateView):
    model = puesto
    form_class = puestoForm
    template_name = 'crudperins/puesto_form.html'
    success_url = reverse_lazy('puestos:puesto_listar')
class puestoList(ListView):
    queryset = puesto.objects.order_by('id_puesto')
    template_name = 'crudperins/puesto_list.html'
class puestoUpdate(UpdateView):
    model = puesto
    form_class = puestoForm
    template_name = 'crudperins/puesto_form.html'
    success_url = reverse_lazy('puestos:puesto_listar')
class puestoDelete(DeleteView):
    model = puesto
    template_name = 'crudperins/puesto_delete.html'
    success_url = reverse_lazy('puestos:puesto_listar')
class puestoShow(DeleteView):
    model = puesto
    template_name = 'crudperins/puesto_show.html'
def search_V(request):
    puesto_list = puesto.objects.all()
    puesto_filter = puestoFilter(request.GET, queryset=puesto_list)
    return render(request, 'crudperins/puesto_list_filter.html', {'filter': puesto_filter})


#-----------------------------view karyn-------------------------------------
class grupoCreate(CreateView):
    model = grupo
    form_class = grupoForm
    template_name = 'crudperins/grupo_form.html'
    success_url = reverse_lazy('grupos:grupo_listar')
class grupoList(ListView):
    queryset = grupo.objects.order_by('id_grupo')
    template_name = 'crudperins/grupo_list.html'
    paginate_by = 10
class grupoUpdate(UpdateView):
    model = grupo
    form_class = grupoForm
    template_name = 'crudperins/grupo_form.html'
    success_url = reverse_lazy('grupos:grupo_listar')
class grupoDelete(DeleteView):
    model = grupo
    template_name = 'crudperins/grupo_delete.html'
    success_url = reverse_lazy('grupos:grupo_listar')
class grupoShow(DetailView):
    model = grupo
    template_name = 'crudperins/grupo_show.html'
def gruposearch(request):
    grupo_list = grupo.objects.all()
    grupo_filter = grupoFilter(request.GET, queryset=grupo_list)
    return render(request, 'crudperins/grupo_list_filter.html', {'filter': grupo_filter})
#inicia otra vista
class muniCreate(CreateView):
    model = municipio
    form_class = municipioForm
    template_name = 'crudperins/muni_form.html'
    success_url = reverse_lazy('municipios:muni_listar')
class muniList(ListView):
    queryset = municipio.objects.order_by('id_municipio')
    template_name = 'crudperins/muni_list.html'
    paginate_by = 10
class muniUpdate(UpdateView):
    model = municipio
    form_class = municipioForm
    template_name = 'crudperins/muni_form.html'
    success_url = reverse_lazy('municipios:muni_listar')
class muniDelete(DeleteView):
    model = municipio
    template_name = 'crudperins/muni_delete.html'
    success_url = reverse_lazy('municipios:muni_listar')
class muniShow(DetailView):
    model = municipio
    template_name = 'crudperins/muni_show.html'
def munisearch(request):
    muni_list = municipio.objects.all()
    muni_filter = municipioFilter(request.GET, queryset=muni_list)
    return render(request, 'crudperins/muni_list_filter.html', {'filter': muni_filter})


#----------------------view litzy---------------------------
class actividadCreate(CreateView):
    model = actividad
    form_class = actividadForm
    template_name = 'crudperins/actividad_form.html'
    success_url = reverse_lazy('actividades:actividad_listar')
class actividadList(ListView):
    queryset = actividad.objects.order_by('nombre')
    template_name = 'crudperins/actividad_list.html'
class actividadUpdate(UpdateView):
    model = actividad
    form_class = actividadForm
    template_name = 'crudperins/actividad_form.html'
    success_url = reverse_lazy('actividades:actividad_listar')
class actividadDelete(DeleteView):
    model = actividad
    template_name = 'crudperins/actividad_delete.html'
    success_url = reverse_lazy('actividades:actividad_listar')
class actividadShow(DetailView):
    model = actividad
    template_name = 'crudperins/actividad_show.html'
def searchL(request):
    actividad_list = actividad.objects.all()
    actividad_filter = actividadFilter(request.GET, queryset=actividad_list)
    return render(request, 'crudperins/actividades_list_filter.html', {'filter': actividad_filter})
#inicia otra vista
class rolCreate(CreateView):
    model = rol
    form_class = rolForm
    template_name = 'crudperins/rol_form.html'
    success_url = reverse_lazy('roles:rol_listar')
class rolList(ListView):
    queryset = rol.objects.order_by('id_rol')
    template_name = 'crudperins/rol_list.html'
class rolUpdate(UpdateView):
    model = rol
    form_class = rolForm
    template_name = 'crudperins/rol_form.html'
    success_url = reverse_lazy('roles:rol_listar')
class rolDelete(DeleteView):
    model = rol
    template_name = 'crudperins/rol_delete.html'
    success_url = reverse_lazy('roles:rol_listar')
class rolShow(DetailView):
    model = rol
    template_name = 'crudperins/rol_show.html'
def search_L(request):
    rol_list = rol.objects.all()
    rol_filter = rolFilter(request.GET, queryset=rol_list)
    return render(request, 'crudperins/rol_list_filter.html', {'filter': rol_filter})


#------------------------------view amairany---------------------
class carreraCreate(CreateView):
    model = carrera
    form_class = carreraForm
    template_name = 'crudperins/carrera_form.html'
    success_url = reverse_lazy('carrera:carrera_listar')
class carreraList(ListView):
    queryset = carrera.objects.order_by('clave_oficial')
    template_name = 'crudperins/carrera_list.html'
class carreraUpdate(UpdateView):
    model = carrera
    form_class = carreraForm
    template_name = 'crudperins/carrera_form.html'
    success_url = reverse_lazy('carrera:carrera_listar')
class carreraDelete(DeleteView):
    model = carrera
    template_name = 'crudperins/carrera_delete.html'
    success_url = reverse_lazy('carrera:carrera_listar')
class carreraShow(DetailView):
    model = carrera
    template_name = 'crudperins/carrera_show.html'
def searchM(request):
    carrera_list = carrera.objects.all()
    carrera_filter = carreraFilter(request.GET, queryset=carrera_list)
    return render(request, 'crudperins/carrera_list_filter.html', {'filter': carrera_filter})
#inicia otra vista
class localidadCreate(CreateView):
    model = localidad
    form_class = localidadForm
    template_name = 'crudperins/localidad_form.html'
    success_url = reverse_lazy('localidad:localidad_listar')
class localidadList(ListView):
    queryset = localidad.objects.order_by('id_localidad')
    template_name = 'crudperins/localidad_list.html'
class localidadUpdate(UpdateView):
    model = localidad
    form_class = localidadForm
    template_name = 'crudperins/localidad_form.html'
    success_url = reverse_lazy('localidad:localidad_listar')
class localidadDelete(DeleteView):
    model = localidad
    template_name = 'crudperins/localidad_delete.html'
    success_url = reverse_lazy('localidad:localidad_listar')
class localidadShow(DetailView):
    model = localidad
    template_name = 'crudperins/localidad_show.html'
def buscarM(request):
    localidad_list = localidad.objects.all()
    localidad_filter = localidadFilter(request.GET, queryset=localidad_list)
    return render(request, 'crudperins/localidad_list_filter.html', {'filter': localidad_filter})


#-------------------------------------------view nubia-------------------------
class coordinadorCreate(CreateView):
    model = coordinador
    form_class = coordinadorForm
    template_name = 'crudperins/coordinador_form.html'
    success_url = reverse_lazy('coordinadores:coordinar_listar')

class coordinadorList(ListView):
    queryset = coordinador.objects.order_by('usuario')
    template_name = 'crudperins/coordinador_list.html'
    paginate_by = 10

class coordinadorUpdate(UpdateView):
    model = coordinador
    form_class = coordinadorForm
    template_name = 'crudperins/coordinador_form.html'
    success_url = reverse_lazy('coordinadores:coordinar_listar')

class coordinadorDelete(DeleteView):
    model = coordinador
    template_name = 'crudperins/coordinador_delete.html'
    success_url = reverse_lazy('coordinadores:coordinar_listar')

class coordinadorShow(DetailView):
    model = coordinador
    template_name = 'crudperins/coordinador_show.html'

def search_c(request):
    coordinador_list = coordinador.objects.all()
    coordinador_filter = coordinadorFilter(request.GET, queryset=coordinador_list)
    return render(request, 'crudperins/coordinador_list_filter.html', {'filter': coordinador_filter})

#aqui inician las vistas del crud instructor

class instructorCreate(CreateView):
    model = instructor
    form_class = instructorForm
    template_name = 'crudperins/instructor_form.html'
    success_url = reverse_lazy('instructores:instrucciones_listar')


class instructorList(ListView):
    queryset = instructor.objects.order_by('id_instructor')
    template_name = 'crudperins/instructor_list.html'
    paginate_by = 10


class instructorUpdate(UpdateView):
    model = instructor
    form_class = instructorForm
    template_name = 'crudperins/instructor_form.html'
    success_url = reverse_lazy('instructores:instrucciones_listar')


class instructorDelete(DeleteView):
    model = instructor
    template_name = 'crudperins/instructor_delete.html'
    success_url = reverse_lazy('instructores:instrucciones_listar')


class instructorShow(DetailView):
    model = instructor
    template_name = 'crudperins/instructor_form.html'

def search_i(request):
    instructor_list = instructor.objects.all()
    instructor_filter = instructorFilter(request.GET, queryset=instructor_list)
    return render(request, 'crudperins/instructor_list_filter.html', {'filter': instructor_filter})

