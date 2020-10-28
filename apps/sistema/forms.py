from django import forms
from apps.sistema.models import Productos, Contratos, Transporte, Pedido, ProcesPedido, Seguimiento
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserChangeForm


class RegistroDeProductos(forms.ModelForm):
	class Meta:
		model = Productos

		fields = [
		'nom_prod',
		'precio_prod',
		'desc_prod',
		'stock_prod',
		'usuarios_usuarios_id_user',
		]

		labels = {
		'nom_prod':'Nombre del producto',
		'precio_prod':'Precio del producto',
		'desc_prod':'Descripcion del producto',
		'stock_prod':'Stock',
		'usuarios_usuarios_id_user':'Vendedor',
		}

		widgets = {
		'nom_prod': forms.TextInput(attrs={'class':'form-control col-10'}),
		'precio_prod': forms.TextInput(attrs={'class':'form-control col-10'}),
		'desc_prod' : forms.TextInput(attrs={'class':'form-control col-10'}),
		'stock_prod': forms.TextInput(attrs={'class':'form-control col-10'}),
		'usuarios_usuarios_id_user': forms.TextInput(attrs={'class':'form-control'}),
		}


class NuevoContrato(forms.ModelForm):
	class Meta:
		model = Contratos

		fields = [
		'usuarios_usuarios_id_user',
		'rut_person',
		'phone_contrat',
		]

		labels = {
		'usuarios_usuarios_id_user':'id usuario',
		'rut_person':'rut',
		'phone_contrat':'numero de telefono',
		}

		widgets = {
		'usuarios_usuarios_id_user':forms.TextInput(attrs={'class':'form-control col-10'}),
		'rut_person': forms.TextInput(attrs={'class':'form-control col-10'}),
		'phone_contrat': forms.TextInput(attrs={'class':'form-control col-10'}),
		}



class editContrato(UserChangeForm):
	class Meta:
		model = Contratos

		fields = [

		'estado',
		'rut_person',
		'phone_contrat',
		'emision_contrat',
		'fin_contrat',
		]

		labels = {
		'estado' : 'estado',
		'rut_person' : 'rut',
		'phone_contrat':'telefono',
		'emision_contrat':'emision',
		'fin_contrat':'termino',
		}



class RegistroDeTransportes(forms.ModelForm):
	class Meta:
		model = Transporte

		fields = [
		'usuarios_usuarios_id_user',
		'tip_transporte',
		'tamano_trans',
		'capacidad_trans',
		'refrigeracion_trans',
		'fecha_trans',
		]

		labels = {
		'usuarios_usuarios_id_user':'id usuario',
		'tip_transporte':'tipo de transporte',
		'tamano_trans':'tamaño de transporte',
		'capacidad_trans':'capacidad',
		'refrigeracion_trans':'refrigeracion',
		'fecha_trans':'fecha',
		}

		widgets = {
		'usuarios_usuarios_id_user': forms.TextInput(attrs={'class':'form-control col-10'}),
		'tip_transporte': forms.TextInput(attrs={'class':'form-control col-10'}),
		'tamano_trans': forms.TextInput(attrs={'class':'form-control col-10'}),
		'capacidad_trans' : forms.TextInput(attrs={'class':'form-control col-10'}),
		'refrigeracion_trans': forms.TextInput(attrs={'class':'form-control col-10'}),
		'fecha_trans': forms.DateInput(),
		}



class SolicitarPedido(forms.ModelForm):
	class Meta:
		model = Pedido

		fields = [
		'tipo',
    	'fecha',
    	'descrip',
    	'usuarios_usuarios_id_user',
		]

		labels = {
		'tipo' : 'tipo de producto',
    	'fecha':'fecha',
    	'descrip':'descripcion',
    	'usuarios_usuarios_id_user':'usuario',
		}

		widgets = {
		'tipo': forms.TextInput(attrs={'class':'form-control col-10'}),
    	'fecha': forms.DateInput(),
    	'descrip': forms.TextInput(attrs={'class':'form-control col-10'}),
    	'usuarios_usuarios_id_user': forms.TextInput(attrs={'class':'form-control col-10'}),
		}


class AprobarPedidos(UserChangeForm):
	class Meta:
		model = Pedido

		fields = [
		'tipo',
    	'fecha',
    	'descrip',
    	'estado_admin',
		]

		labels = {
		'tipo' : 'tipo de producto',
    	'fecha':'fecha',
    	'descrip':'descripcion',
    	'estado_admin' : 'estado',
		}

		widgets = {
		'tipo': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
    	'fecha': forms.DateInput(),
    	'descrip': forms.TextInput(attrs={'class':'form-control col-10','readonly':'True'}),
		}




class OfrecerProductos(UserChangeForm):
	class Meta:
		model = Pedido

		fields = [
		'tipo',
    	'fecha',
    	'descrip',
    	'productos_id_prod',
		]

		labels = {
		'tipo' : 'tipo de producto',
    	'fecha':'fecha',
    	'descrip':'descripcion',
    	'productos_id_prod' : 'lista de productos',
		}

		widgets = {
		'tipo': forms.TextInput(attrs={'class':'form-control col-10'}),
    	'fecha': forms.DateInput(),
    	'descrip': forms.TextInput(attrs={'class':'form-control col-10'}),
		}




class ResponderOferta(UserChangeForm):
	class Meta:
		model = Pedido

		fields = [
		'tipo',
    	'fecha',
    	'descrip',
    	'productos_id_prod',
    	'estado_productor',
		]

		labels = {
		'tipo' : 'tipo de producto',
    	'fecha':'fecha',
    	'descrip':'descripcion',
    	'productos_id_prod' : 'lista de productos',
    	'estado_productor' : 'estado',
		}

		widgets = {
		'tipo': forms.TextInput(attrs={'class':'form-control col-10'}),
    	'fecha': forms.DateInput(),
    	'descrip': forms.TextInput(attrs={'class':'form-control col-10'}),
		}



class OfrecerTransport(forms.ModelForm):
	class Meta:
		model = ProcesPedido

		fields = [
		'transporte_id_trans',
		'pedido_id_ped',
		]

		labels = {
		'transporte_id_trans':'Transporte',
		'pedido_id_ped':'pedido',
		}

		widgets = {
    	'pedido_id_ped': forms.TextInput(attrs={'class':'form-control col-10'}),
		}



class ResponderTransporte(UserChangeForm):
	class Meta:
		model = ProcesPedido

		fields = [
		'transporte_id_trans',
		'estado_proceso',
		]

		labels = {
		'transporte_id_trans':'Transporte',
		'estado_proceso':'Estado',
		}

		widgets = {
		'transporte_id_trans': forms.TextInput(attrs={'class':'form-control col-10'}),
		}



class SolicitarSeguimiento(forms.ModelForm):
	class Meta:
		model = Seguimiento

		fields = [
		'pedido_id_ped',
		'proces_pedido_id_proc_pedido',
		]

		labels = {
		'pedido_id_ped':'pedido',
		'proces_pedido_id_proc_pedido':'proceso',
		}
		widgets = {
		'pedido_id_ped': forms.TextInput(attrs={'class':'form-control col-10'}),
		'proces_pedido_id_proc_pedido': forms.TextInput(attrs={'class':'form-control col-10'}),
		}


class EditarSeguimiento(UserChangeForm):
	class Meta:
		model = Seguimiento

		fields = [
		'est_seguimiento',
		]
