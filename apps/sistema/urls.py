from django.conf.urls import url, include
from apps.sistema.views import index,listar_usuarios,User_edit,registrarproductos,listar_productos

from django.urls import include, path

app_name = "sistema";

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^usuarios/', listar_usuarios,name='usuarios'),
    url(r'^editar/(?P<id_user>\d*)$', User_edit, name='editar_usuario'),
    url(r'^registrarprod/', registrarproductos,name='regprod'),
    url(r'^listaprod/', listar_productos, name='listaprod'),
]