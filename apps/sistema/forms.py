from django import forms
from apps.sistema.models import Productos


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
