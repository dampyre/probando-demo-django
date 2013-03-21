from django.db import models
# Create your models here.
# se crea el modelo para manejar clientes en el admin


class cliente(models.Model):
    # se crea la clase cliente que hereda los modelos de models.Model
    # django lo maneja como campos de la bdd
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    status = models.BooleanField(default=True)    #se deja en true para habilitar el usuario por defecto

    def __unicode__(self):
        nombreCompleto = "%s %s" % (self.nombre, self.apellidos)
        return nombreCompleto
# se crea el modelo para manejar productos en el admin y en vistas


class producto(models.Model):
    def url(self,filename): 
        ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
        return ruta

    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    status      = models.BooleanField(default=True)
    # null=True,blank=True = para poder guardar sin subir imagen 
    imagen      = models.ImageField(upload_to=url, null=True,blank=True)
    precio      = models.DecimalField(max_digits=6, decimal_places=2)
    stock       = models.IntegerField()

    def __unicode__(self):
        return self.nombre


