# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import producto
from demo.apps.home.forms import ContactForm, LoginForm
# para envio correo se importa  // envia HTML
#from django.core.mail import EmailMultiAlternatives
# importamos clases para manejar login
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
# importamos el core del paginator
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	mensaje ="mensaje desde las vistas"
	ctx={'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))
# vista para productos
def productos_view(request, pagina):
	lista_prod = producto.objects.filter(status=True)
	# es igual a select * from ventas_productos where status=True
	# paginator = Paginator(lista_prod,3) #cantidad de productos se requieren por pagina
	paginator = Paginator(lista_prod,3)
	try:
	 		page = int(pagina)
	except:
	         page = 1
	try:
		productos = paginator.page(page)
	except(EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)
	ctx = {'productos':productos}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))
def singleProduct_view(request,id_prod):
	prod = producto.objects.get(id=id_prod)
	ctx =  {'producto': prod}
	return render_to_response('home/SingleProducto.html',ctx,context_instance=RequestContext(request))
def contacto_view(request):
	info_enviado = False #define si se envio la info o no
	email= ""
	titulo=""
	texto=""
	if request.method == "POST": # evalua si se envio algo por el metodo POST
		formulario = ContactForm(request.POST)
		if formulario.is_valid(): # si lo que se envio es valido corresponde a validacion
			info_enviado = True #ahora el formulario es true
			email = formulario.cleaned_data['email']
			titulo = formulario.cleaned_data['titulo']
			texto = formulario.cleaned_data['texto']
			#configuracion envio correo
			# a quien se envia
			# to_admin = 'dampyre@gmail.com'
			# html_content = "infor recivida de[%s] <br><br><br>****MENSAJE****<br><br><br>"%(email,texto)
			# msg = EmailMultiAlternatives('correo de contacto',html_content,'from@server.com',[to_admin])
			# msg.attach_alternative(html_content,'text/html')#definimos el contenido html
			# msg.senf()#se envio el correo
	else:
		formulario = ContactForm()


	
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response ('home/contacto.html',ctx,context_instance=RequestContext(request))


# vista del login de usuario
def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o password incorrecto"
		form = LoginForm()
		ctx = {'form':form, 'mensaje': mensaje}
		return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')