from django.db import models
import datetime
# Create your models here.
class Perfil(models.Model):
	nombre = models.CharField(max_length=200) 
	apellido = models.CharField(max_length=200)
	nick = models.CharField(max_length=100)
	correo = models.EmailField()
	pass_correo = models.CharField(max_length=50)
	cuota_correo = models.IntegerField()
	correo_sec = models.EmailField(null= True)
	pass_correo_sec = models.CharField(max_length=50, null= True)
	ip_usuario = models.IPAddressField (null= True)
	anexo = models.CharField(max_length=10)
	status = models.BooleanField(default= True)
	fecha_ingreso = models.DateField()
	def __unicode__(self):
		
		return self.nick
class Bitacora(models.Model):
	perfil = models.ForeignKey(Perfil)
	fecha_bitacora = models.DateField()
	contenido = models.TextField()

	def __unicode__(self):
		encabezado = "%s %s" % (self.perfil.nick, self.fecha_bitacora)
		return encabezado



