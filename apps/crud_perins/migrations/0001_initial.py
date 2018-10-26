# Generated by Django 2.1.1 on 2018-10-26 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actividad',
            fields=[
                ('nombre', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('objetivo_general', models.TextField()),
                ('competencia', models.TextField()),
                ('temario', models.TextField()),
                ('autorizada', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='alumnos',
            fields=[
                ('nocontrol', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField(verbose_name=20)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
                ('calle', models.CharField(max_length=50)),
                ('numero_exterior', models.CharField(max_length=50)),
                ('numero_interior', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('estatus', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='area',
            fields=[
                ('id_area', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='carrera',
            fields=[
                ('clave_oficial', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre_carrera', models.CharField(max_length=70)),
                ('reticula', models.CharField(max_length=70)),
                ('nivel_escolar', models.CharField(max_length=40)),
                ('nombre_reducido', models.CharField(max_length=10)),
                ('carga_maxima', models.SmallIntegerField(verbose_name=6)),
                ('creditos_totales', models.SmallIntegerField(verbose_name=6)),
                ('nivel', models.CharField(max_length=25)),
                ('modalidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='coordinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id_estado', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='grupo',
            fields=[
                ('id_grupo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_grupo', models.CharField(max_length=15)),
                ('capacidad', models.IntegerField(verbose_name=11)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.area')),
            ],
        ),
        migrations.CreateModel(
            name='inscripcion',
            fields=[
                ('calificacion', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.actividad')),
                ('alumnos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.alumnos')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.area')),
                ('carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.carrera')),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('id_instructor', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=1)),
                ('rfc', models.CharField(max_length=11)),
                ('formacion', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='localidad',
            fields=[
                ('id_localidad', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre_localidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='municipio',
            fields=[
                ('id_municipio', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre_municipio', models.CharField(max_length=70)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.estado')),
            ],
        ),
        migrations.CreateModel(
            name='organigrama',
            fields=[
                ('id_organigrama', models.IntegerField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('area_depende', models.IntegerField(verbose_name=11)),
                ('nivel', models.IntegerField(verbose_name=11)),
                ('tipo_area', models.IntegerField(verbose_name=11)),
                ('titular', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='periodo',
            fields=[
                ('id_periodo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_corto', models.CharField(max_length=50)),
                ('nombre_largo', models.CharField(max_length=30)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='puesto',
            fields=[
                ('id_puesto', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('nivel', models.IntegerField(verbose_name=11)),
                ('tipo', models.CharField(max_length=1)),
                ('funciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id_rol', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('clave', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('estatus', models.CharField(max_length=50)),
                ('organigrama', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.organigrama')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.rol')),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.municipio'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.instructor'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.periodo'),
        ),
        migrations.AddField(
            model_name='coordinador',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.rol'),
        ),
        migrations.AddField(
            model_name='coordinador',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.usuario'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.carrera'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.localidad'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.rol'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.area'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.grupo'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.instructor'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.periodo'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud_perins.usuario'),
        ),
    ]