# Generated by Django 4.2.5 on 2023-10-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConteoRapidoPunto',
            fields=[
                ('IdRescateR', models.AutoField(primary_key=True, serialize=False)),
                ('oficinaRepre', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=10)),
                ('hora', models.CharField(max_length=5)),
                ('aeropuerto', models.BooleanField(default=False)),
                ('carretero', models.BooleanField(default=False)),
                ('tipoVehic', models.CharField(blank=True, max_length=30)),
                ('lineaAutobus', models.CharField(blank=True, max_length=50)),
                ('numeroEcono', models.CharField(blank=True, max_length=50)),
                ('placas', models.CharField(blank=True, max_length=20)),
                ('vehiculoAseg', models.BooleanField(default=False)),
                ('casaSeguridad', models.BooleanField(default=False)),
                ('centralAutobus', models.BooleanField(default=False)),
                ('ferrocarril', models.BooleanField(default=False)),
                ('empresa', models.CharField(blank=True, max_length=150)),
                ('hotel', models.BooleanField(default=False)),
                ('nombreHotel', models.CharField(blank=True, max_length=100)),
                ('puestosADispo', models.BooleanField(default=False)),
                ('juezCalif', models.BooleanField(default=False)),
                ('reclusorio', models.BooleanField(default=False)),
                ('policiaFede', models.BooleanField(default=False)),
                ('dif', models.BooleanField(default=False)),
                ('policiaEsta', models.BooleanField(default=False)),
                ('policiaMuni', models.BooleanField(default=False)),
                ('guardiaNaci', models.BooleanField(default=False)),
                ('fiscalia', models.BooleanField(default=False)),
                ('otrasAuto', models.BooleanField(default=False)),
                ('voluntarios', models.BooleanField(default=False)),
                ('otro', models.BooleanField(default=False)),
                ('presuntosDelincuentes', models.BooleanField(default=False)),
                ('numPresuntosDelincuentes', models.IntegerField()),
                ('municipio', models.CharField(blank=True, max_length=200)),
                ('puntoEstra', models.CharField(blank=True, max_length=250)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('iso3', models.CharField(max_length=3)),
                ('AS_hombres', models.IntegerField()),
                ('AS_mujeresNoEmb', models.IntegerField()),
                ('AS_mujeresEmb', models.IntegerField()),
                ('nucleosFamiliares', models.IntegerField()),
                ('AA_hombres', models.IntegerField()),
                ('AA_mujeresNoEmb', models.IntegerField()),
                ('AA_mujeresEmb', models.IntegerField()),
                ('NNA_A_hombres', models.IntegerField()),
                ('NNA_A_mujeresNoEmb', models.IntegerField()),
                ('NNA_A_mujeresEmb', models.IntegerField()),
                ('NNA_S_hombres', models.IntegerField()),
                ('NNA_S_mujeresNoEmb', models.IntegerField()),
                ('NNA_S_mujeresEmb', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoFuerza',
            fields=[
                ('idEdoFuerza', models.AutoField(primary_key=True, serialize=False)),
                ('oficinaR', models.CharField(max_length=50)),
                ('numPunto', models.IntegerField()),
                ('nomPuntoRevision', models.CharField(max_length=100)),
                ('tipoP', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=300)),
                ('coordenadasTexto', models.CharField(max_length=300)),
                ('latitud', models.FloatField(default=0.0)),
                ('longitud', models.FloatField(default=0.0)),
                ('personalINM', models.IntegerField()),
                ('personalSEDENA', models.IntegerField()),
                ('personalMarina', models.IntegerField()),
                ('personalGuardiaN', models.IntegerField()),
                ('personalOTROS', models.IntegerField()),
                ('vehiculos', models.IntegerField()),
                ('seccion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Frases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('idMunicipio', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=250)),
                ('estadoAbr', models.CharField(max_length=50)),
                ('nomMunicipio', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('idPais', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pais', models.CharField(max_length=250)),
                ('iso3', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PuntosInternacion',
            fields=[
                ('idPuntoInter', models.AutoField(primary_key=True, serialize=False)),
                ('nombrePunto', models.CharField(max_length=100)),
                ('estadoPunto', models.CharField(max_length=100)),
                ('tipoPunto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RescatePunto',
            fields=[
                ('idRescate', models.AutoField(primary_key=True, serialize=False)),
                ('oficinaRepre', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=10)),
                ('hora', models.CharField(max_length=5)),
                ('aeropuerto', models.BooleanField(default=False)),
                ('carretero', models.BooleanField(default=False)),
                ('tipoVehic', models.CharField(blank=True, max_length=30)),
                ('lineaAutobus', models.CharField(blank=True, max_length=50)),
                ('numeroEcono', models.CharField(blank=True, max_length=50)),
                ('placas', models.CharField(blank=True, max_length=20)),
                ('vehiculoAseg', models.BooleanField(default=False)),
                ('casaSeguridad', models.BooleanField(default=False)),
                ('centralAutobus', models.BooleanField(default=False)),
                ('ferrocarril', models.BooleanField(default=False)),
                ('empresa', models.CharField(blank=True, max_length=150)),
                ('hotel', models.BooleanField(default=False)),
                ('nombreHotel', models.CharField(blank=True, max_length=100)),
                ('puestosADispo', models.BooleanField(default=False)),
                ('juezCalif', models.BooleanField(default=False)),
                ('reclusorio', models.BooleanField(default=False)),
                ('policiaFede', models.BooleanField(default=False)),
                ('dif', models.BooleanField(default=False)),
                ('policiaEsta', models.BooleanField(default=False)),
                ('policiaMuni', models.BooleanField(default=False)),
                ('guardiaNaci', models.BooleanField(default=False)),
                ('fiscalia', models.BooleanField(default=False)),
                ('otrasAuto', models.BooleanField(default=False)),
                ('voluntarios', models.BooleanField(default=False)),
                ('otro', models.BooleanField(default=False)),
                ('presuntosDelincuentes', models.BooleanField(default=False)),
                ('numPresuntosDelincuentes', models.IntegerField()),
                ('municipio', models.CharField(blank=True, max_length=200)),
                ('puntoEstra', models.CharField(blank=True, max_length=250)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('iso3', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=150)),
                ('noIdentidad', models.CharField(max_length=50)),
                ('parentesco', models.CharField(blank=True, max_length=50)),
                ('fechaNacimiento', models.CharField(max_length=10)),
                ('sexo', models.BooleanField(default=False)),
                ('numFamilia', models.IntegerField(blank=True)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUser', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=250)),
                ('estado', models.CharField(choices=[('1', 'AGUASCALIENTES'), ('2', 'BAJA CALIFORNIA'), ('3', 'BAJA CALIFORNIA SUR'), ('4', 'CAMPECHE'), ('5', 'COAHUILA'), ('6', 'COLIMA'), ('7', 'CHIAPAS'), ('8', 'CHIHUAHUA'), ('9', 'CDMX'), ('10', 'DURANGO'), ('11', 'GUANAJUATO'), ('12', 'GUERRERO'), ('13', 'HIDALGO'), ('14', 'JALISCO'), ('15', 'EDOMEX'), ('16', 'MICHOACÁN'), ('17', 'MORELOS'), ('18', 'NAYARIT'), ('19', 'NUEVO LEÓN'), ('20', 'OAXACA'), ('21', 'PUEBLA'), ('22', 'QUERÉTARO'), ('23', 'QUINTANA ROO'), ('24', 'SAN LUIS POTOSÍ'), ('25', 'SINALOA'), ('26', 'SONORA'), ('27', 'TABASCO'), ('28', 'TAMAULIPAS'), ('29', 'TLAXCALA'), ('30', 'VERACRUZ'), ('31', 'YUCATÁN'), ('32', 'ZACATECAS')], default='9', max_length=2)),
                ('tipo', models.CharField(choices=[('1', 'Administrador'), ('2', 'Validador'), ('3', 'Capturador')], default='3', max_length=1)),
            ],
        ),
    ]
