from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('demo.apps.ventas.views',
	url(r'^add/producto/$', 'add_product_view', name = "vista_agregar_producto"),
	url(r'^stock/(?P<id_producto>.*)/$', 'ingreso_stock_view', name = "vista_agregar_stock"),
)