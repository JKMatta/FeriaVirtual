from django import forms
from apps.sistema.models import Productos, Contratos
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserChangeForm


class RegistroDeProductos(forms.ModelForm):
	class Meta:
		model = Productos

		fields = [
		'nom_prod',
		'precio_prod',
		'stock_prod',
		'transporte_id_trans',
		'usuarios_usuarios_id_user',
		]

		labels = {
		'nom_prod':'Nombre del producto',
		'precio_prod':'Precio del producto',
		'stock_prod':'Stock',
		'transporte_id_trans':'Transporte',
		'usuarios_usuarios_id_user':'Vendedor',
		}

		widgets = {
		'nom_prod': forms.TextInput(attrs={'class':'form-control col-10'}),
		'precio_prod': forms.TextInput(attrs={'class':'form-control col-10'}),
		'stock_prod': forms.TextInput(attrs={'class':'form-control col-10'}),
		'transporte_id_trans' : forms.TextInput(attrs={'class':'form-control col-10'}),
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


