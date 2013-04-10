from django.db import models
import datetime
# Create your models here.
# Datos Base de impresora

# ------------------------------------

# marca de la impresora
class marca_modelo(models.Model):
	nombre = models.CharField(max_length= 100)	
 	modelo= models.CharField(max_length= 100)
 	def __unicode__(self):
 		return self.nombre
# ------------------------------------

# datos de la conexion usb-wifi-red-otro
class Conexion(models.Model):
	tipo_conexion = models.CharField(max_length= 100)
	def __unicode__(self):
 		return self.tipo_conexion
# ------------------------------------

# tipo de impresion laser, inkjet etc
class Tipo_impresion(models.Model):
	tipo_impre = models.CharField(max_length= 100)
	def __unicode__(self):
 		return self.tipo_impre
# ------------------------------------
# Estado de trabajo buena mala inactiva
class Estado(models.Model):
	estado = models.CharField(max_length= 100)
	def __unicode__(self):
 		return self.estado

class Impresora(models.Model):
	serialn = models.CharField(max_length= 100, null= True)
	nombre = models.ForeignKey(marca_modelo)
	tipo_conexion= models.ForeignKey(Conexion)
	tipo_impre = models.ForeignKey(Tipo_impresion)
	estado = models.ForeignKey(Estado)
	fecha_ingreso = models.DateField()
	def __unicode__(self):
		tipo= "%s %s" % (self.nombre.modelo, self.serialn)
 		return tipo
