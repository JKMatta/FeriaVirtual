from django.conf.urls import url, include
from apps.sistema.views import index,listar_usuarios,User_edit,registrarproductos,listar_productos,Contrato,VerContrato,registrartransportes
from apps.sistema.views import solicitarpedido,listar_pedidos,AdministrarPedido,OfertaProducto,lista_ofrecer,lista_procesopedidos,ResponderOfertas
from apps.sistema.views import lista_sin_transporte,OfertarTransporte,lista_en_proceso,ResponderTransportes,Eliminar_ofert_transport,SolicitarSeguimientos
from apps.sistema.views import lista_en_seguimiento,seguimiento_admin,AdministrarSeguimientos
from django.urls import include, path

app_name = "sistema";

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^usuarios/', listar_usuarios,name='usuarios'),
    url(r'^editar/(?P<id_user>\d*)$', User_edit, name='editar_usuario'),
    url(r'^registrarprod/', registrarproductos,name='regprod'),
    url(r'^listaprod/', listar_productos, name='listaprod'),
    url(r'^mi-contrato/',VerContrato,name='mi-contrato'),
    url(r'^contrato/', Contrato, name='regcontr'),
    url(r'^registrartrans/', registrartransportes,name='regptrans'),
    url(r'^solicitar-pedido/', solicitarpedido,name='solped'),
    url(r'^listapedid/', listar_pedidos, name='listaped'),
    url(r'^administrar-pedido/(?P<id_ped>\d*)$', AdministrarPedido, name='administrarpedido'),
    url(r'^lista-sin-ofertas/', lista_ofrecer, name='listasinofertas'),
    url(r'^oferta-transporte/(?P<id_ped>\d*)$', OfertaProducto, name='ofertatransporte'),
    url(r'^mis-pedidos/', lista_procesopedidos, name='mispedidos'),
    url(r'^responder-oferta/(?P<id_ped>\d*)$', ResponderOfertas, name='responderoferta'),
    url(r'^listar-ofertas/', lista_sin_transporte, name='listaparaofertar'),
    url(r'^ofrecer-transporte/(?P<id_ped>\d*)$', OfertarTransporte, name='ofrecertrans'),
    url(r'^listar-proceso/', lista_en_proceso, name='listaproceso'),
    url(r'^responder-transport/(?P<id_proc_pedido>\d*)$', ResponderTransportes, name='respondertransport'),
    url(r'^eliminar-oferta/(?P<id_proc_pedido>\d*)$', Eliminar_ofert_transport, name='eliminaroferta'),
    url(r'^solicitar-seg/(?P<id_proc_pedido>\d*)$', SolicitarSeguimientos, name='solicitarseg'),
    url(r'^mis-seguimientos/', lista_en_seguimiento, name='misseguimientos'),
    url(r'^lista-seguimiento/', seguimiento_admin, name='listaseguimientos'),
    url(r'^administrar-seguimiento/(?P<id_seguimiento>\d*)$', AdministrarSeguimientos, name='administrarseguimiento'),
]


