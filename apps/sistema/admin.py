from django.contrib import admin
from .models import Productos, Contratos, Transporte, Pedido, ProcesPedido, Seguimiento

#Register your models here.

admin.site.register(Productos)
admin.site.register(Contratos)
admin.site.register(Transporte)
admin.site.register(Pedido)
admin.site.register(ProcesPedido)
admin.site.register(Seguimiento)