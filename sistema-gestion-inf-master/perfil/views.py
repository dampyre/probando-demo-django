# Create your views here.
from perfil.models import Perfil, Bitacora
from django.template import RequestContext
from django.shortcuts import render_to_response

def lista_usuarios(request):
	usuarios= Perfil.objects.all()
	ctx= {'lista':usuarios}
	return render_to_response('lista_usuarios.html',ctx)
def lista_bitacora(request):
	bitacora = Bitacora.objects.all()
	ctx= {'registro': bitacora}
	return render_to_response('lista_usuarios.html',ctx)
