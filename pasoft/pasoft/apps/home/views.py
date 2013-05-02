# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from pasoft.apps.ventas.models import producto
def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

#def about_view(request):
#	return render_to_response('home/about.html', context_instance=RequestContext(request))

#como pasar invormacion de vistas a html

def about_view(request):
	#para enviar un mensaje
	mensaje = "esto es un mensaje desde mi vista"
	ctx={'msg':mensaje}
	return render_to_response('home/about.html', ctx,context_instance=RequestContext(request))

def productos_view(request):
	#primero importar pasoft.apps.ventas.models import producto --> ver arriva
	#traer a todos los productos activos: select *  from ventas_productos where status = true
	prod = producto.objects.filter(status=True)
	ctx = {'productos':prod}
	return render_to_response('home/productos.html',ctx, context_instance=RequestContext(request))