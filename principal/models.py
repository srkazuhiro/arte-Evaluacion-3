from django.db import models

# Create your models here.
class Categoria(models.Model):
    Categoria_id=models.AutoField(primary_key=True, verbose_name='idCategoria')
    nombrecategoria=models.CharField(max_length=40,verbose_name='NombreCategoria')

class Ilustracion(models.Model):
    Ilustracion_id=models.AutoField(primary_key=True, verbose_name='idIlustracion')
    Tipoymodelo=models.CharField(max_length=100,verbose_name='Tipoymodelo' )
    Editor=models.CharField(max_length=60, verbose_name='Editor')
    fecha=models.DateField(verbose_name='fechaIlustracion')
    Categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

class Imagenes(models.Model):
    Imagen_id=models.AutoField(primary_key=True, verbose_name="idImagen")
    Ilustracion=models.ForeignKey(Ilustracion, on_delete=models.CASCADE)

class Editor(models.Model):
    rut=models.CharField(max_length=10, primary_key=True,verbose_name='Rut')
    nombre=models.CharField(max_length=50,verbose_name='nombreeditor')
    telefono=models.IntegerField(verbose_name='numeroeditor')

