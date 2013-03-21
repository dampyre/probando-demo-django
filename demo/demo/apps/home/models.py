from django.db import models
# importando modelo de auditoria de usuarios
from django.contrib.auth.models import User
# Create your models here.

      
class userProfile(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
		return ruta
	user  		= models.OneToOneField(User)
	# modelo OneToOneField permite generar un unico perfil o un registro unico
	# llave foreana 
	photo		= models.ImageField(upload_to=url)
	telefono 	= models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username
