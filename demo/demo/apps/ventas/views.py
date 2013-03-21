from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm, formStock
from demo.apps.ventas.models import producto
from django.http import HttpResponseRedirect

def add_product_view(request):
    info = "inicializando"
    if request.user.is_authenticated():
        if request.method == "POST":
            #si es post es por que estan enviando info
            #se crea un nuevo formulario se asigna a una variable
            #se le pasa la inforpacion que va en el metodo post
            form = addProductForm(request.POST,request.FILES)
            # se crea un variable con valor de estado

            if form.is_valid():
            #si el formulario es valido
                nombre = form.cleaned_data['nombre']
                descripcion = form.cleaned_data['descripcion']
                imagen = form.cleaned_data['imagen'] # se obtiene del envio de formulario request.FILE
                precio = form.cleaned_data['precio']
                stock = form.cleaned_data['stock']
                p = producto()    #se crea el objeto producto
                if imagen: #se genera una validacion
                    p.imagen = imagen
                p.nombre        = nombre
                p.descripcion   = descripcion
                p.precio        = precio
                p.stock         = suma   
                p.status = True
                p.save()    #Guarda la informacion
                info = "Datos guardados"
            else:
                info = "info erronea"
        form = addProductForm()
        ctx = {'form': form, 'informacion':info}
        return render_to_response('ventas/addProducto.html', ctx, context_instance=RequestContext(request))


    else:

        return HttpResponseRedirect('/')
def Ingreso_stock_view(request, id_producto):
    prod = producto.objects.get(id=id_producto)

    return render_to_response('ventas/agregaStock.html', context_instance=RequestContext(request))
