from django.db import models
# Create your models here.


class carrera(models.Model):
    clave_oficial = models.CharField(max_length=15,primary_key=True)
    nombre_carrera = models.CharField(max_length=70)
    reticula = models.CharField(max_length=70)
    nivel_escolar = models.CharField(max_length=40)
    nombre_reducido = models.CharField(max_length=10)
    carga_maxima = models.SmallIntegerField(6)
    creditos_totales = models.SmallIntegerField(6)
    nivel = models.CharField(max_length=25)
    modalidad = models.CharField(max_length=30)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos
    def __str__(self):
        return '{}'.format(self.nombre_carrera)


class estado(models.Model):
    id_estado = models.SmallIntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=70)
# aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre_estado)


class municipio(models.Model):
    id_municipio = models.SmallIntegerField(primary_key=True)
    nombre_municipio = models.CharField(max_length=70)
    estado = models.ForeignKey(estado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_municipio)


class localidad(models.Model):
    id_localidad = models.BigIntegerField(primary_key=True)
    nombre_localidad = models.CharField(max_length=50)
    municipio = models.ForeignKey(municipio, null=True, blank=True, on_delete=models.CASCADE)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre_localidad)


class rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    descripcion=models.TextField()
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre_rol)


class organigrama(models.Model):
    id_organigrama=models.IntegerField(primary_key=True)
    area=models.CharField(max_length=60)
    descripcion=models.TextField()
    area_depende=models.IntegerField(11)
    nivel=models.IntegerField(11)
    tipo_area=models.IntegerField(11)
    titular=models.CharField(max_length=60)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.area)


class usuario(models.Model):
    clave = models.CharField(max_length=30,primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    estatus = models.CharField(max_length=50)
    rol = models.ForeignKey(rol, null=True, blank=True, on_delete=models.CASCADE)
    organigrama = models.ForeignKey(organigrama, null=True, blank=True, on_delete=models.CASCADE)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre)


class periodo(models.Model):
    id_periodo = models.IntegerField(primary_key=True)
    nombre_corto = models.CharField(max_length=50)
    nombre_largo = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    status = models.CharField(max_length=30)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
            return '{}'.format(self.nombre_corto)


class instructor(models.Model):
    id_instructor = models.SmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    rfc = models.CharField(max_length=11)
    formacion = models.CharField(max_length=70)
     # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre)


class area(models.Model):
    id_area = models.IntegerField(primary_key=True)
    nombre_area = models.CharField(max_length=20)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre_area)


class grupo(models.Model):
    id_grupo = models.IntegerField(primary_key=True)
    nombre_grupo = models.CharField(max_length=15)
    capacidad = models.IntegerField(11)
    area = models.ForeignKey(area, null=True, blank=True, on_delete=models.CASCADE)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre_grupo)


class actividad(models.Model):
    nombre = models.SmallIntegerField(primary_key=True)
    objetivo_general= models.TextField()
    competencia= models.TextField()
    temario= models.TextField()
    autorizada= models.CharField(max_length=1)
    usuario = models.ForeignKey(usuario, null=True, blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(periodo, null=True, blank=True, on_delete=models.CASCADE)
    instructor = models.ForeignKey(instructor, null=True, blank=True, on_delete=models.CASCADE)
    grupo = models.ForeignKey(grupo, null=True, blank=True, on_delete=models.CASCADE)
    area = models.ForeignKey(area, null=True, blank=True, on_delete=models.CASCADE)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.objetivo_general)


class alumnos(models.Model):
    nocontrol = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telefono = models.BigIntegerField(20)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    calle = models.CharField(max_length=50)
    numero_exterior = models.CharField(max_length=50)
    numero_interior = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    estatus = models.CharField(max_length=1)
    carrera = models.ForeignKey(carrera, null=True, blank=True, on_delete=models.CASCADE)
    localidad = models.ForeignKey(localidad, null=True, blank=True, on_delete=models.CASCADE)
    rol = models.ForeignKey(rol, null=True, blank=True, on_delete=models.CASCADE)
     # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre)


class inscripcion(models.Model):
    calificacion = models.SmallIntegerField(primary_key=True)
    periodo = models.ForeignKey(periodo, null=True, blank=True, on_delete=models.CASCADE)
    actividad = models.ForeignKey(actividad, null=True, blank=True, on_delete=models.CASCADE)
    instructor = models.ForeignKey(instructor, null=True, blank=True, on_delete=models.CASCADE)
    carrera = models.ForeignKey(carrera, null=True, blank=True, on_delete=models.CASCADE)
    grupo = models.ForeignKey(grupo, null=True, blank=True, on_delete=models.CASCADE)
    area = models.ForeignKey(area, null=True, blank=True, on_delete=models.CASCADE)
    alumnos = models.ForeignKey(alumnos, null=True, blank=True, on_delete=models.CASCADE)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.calificacion)


class coordinador(models.Model):
    usuario = models.ForeignKey(usuario, null=True, blank=True, on_delete=models.CASCADE)
    rol = models.ForeignKey(rol, null=True, blank=True, on_delete=models.CASCADE)
    carrera = models.ForeignKey(carrera, null=True, blank=True, on_delete=models.CASCADE)


class puesto(models.Model):
    id_puesto = models.IntegerField(primary_key=True)
    descripcion = models.TextField()
    nivel = models.IntegerField(11)
    tipo = models.CharField(max_length=1)
    funciones = models.TextField()
