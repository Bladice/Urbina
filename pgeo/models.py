import datetime
from django.db import models

# Create your models here.

class Rutas(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Ruta')
    detalle = models.CharField(max_length=200, verbose_name='Descripción')
    imagen = models.ImageField(upload_to="static/image")
    nivel = models.CharField(max_length=30, blank=True, verbose_name='Nivel Ruta')
    url = models.URLField(blank=True)
    fecha = models.DateField(auto_created=False, auto_now_add=True, verbose_name='Fecha Registro')
    act = models.IntegerField(default=0, verbose_name='Actividad')
    length_unit = models.CharField(max_length=5, default='Km', verbose_name='Unidad')
    length = models.IntegerField(default=0, verbose_name='Distancia')
    near = models.CharField(max_length=100, blank=True, verbose_name='Cerca de')
    author = models.CharField(max_length=100, default='GAD Presidente Urbina', verbose_name='Autor')
    estado = models.BooleanField(default=True, verbose_name='Activo/Inactivo')

    def __str__(self):
        return self.nombre


baja = [
    ('A', 'Activo'),
    ('D', 'Desactivar')
]


class Foto_ruta(models.Model):
    ruta = models.ForeignKey(Rutas, on_delete=models.CASCADE, verbose_name='Ruta')
    detalle = models.CharField(max_length=200, blank=True, verbose_name='Descripcion')
    foto = models.ImageField(upload_to='static/image', verbose_name='Foto')
    fecha_crea = models.DateField( auto_created=False, auto_now_add=True, verbose_name='Fecha de Ingreso')
    estado = models.CharField(max_length=1, choices=baja, default='A', verbose_name='Estado')

    def __str__(self):
        return self.detalle

tipo = [
    ('Ciclismo', 'Ciclismo'),
    ('Granjas', 'Granjas'),
    ('Gastronomia', 'Gastronomia'),
    ('Entretenimiento', 'Entretenimiento'),
    ('Emprendimientos', 'Emprendimientos')
]

class Empresa(models.Model):
    ruta = models.ForeignKey(Rutas, on_delete=models.CASCADE, verbose_name='Ruta')
    nombre = models.CharField(max_length=100, verbose_name='Nombre Empresa')
    detalle = models.TextField(blank=True, verbose_name='Breve Reseña')
    foto = models.ImageField(upload_to='static/image', blank=True, verbose_name='Foto Lugar')
    propietario = models.CharField(max_length=60, blank=True, verbose_name='Propietario')
    direccion = models.CharField(max_length=200, blank=False, verbose_name='Dirección')
    correo = models.EmailField(max_length=100, blank=False, verbose_name='Email')
    telefono = models.CharField(max_length=10, blank=True, verbose_name='Telefono')
    celular = models.CharField(max_length=10, blank=False, verbose_name='celular')
    video2 = models.FileField(upload_to='static/image', blank=True, verbose_name='Video')
    fecha_creacion = models.DateField(default=datetime.date.today, verbose_name='Activación')

    def __str__(self):
        return '%s %s ' % (self.ruta.nombre, self.nombre)

class Foto_empresa(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    foto = models.ImageField(upload_to='static/image', blank=True, verbose_name='Fotos')
    fecha_ing = models.DateField(default=datetime.date.today, verbose_name='Fecha de Ingreso')
    estado = models.CharField(max_length=1, choices=baja, default='A', verbose_name='Estado')

    def __str__(self):
        return '%s %s ' % (self.empresa.nombre, self.empresa.ruta.nombre)