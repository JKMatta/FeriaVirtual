# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class DatPersonal(models.Model):
    id_dat = models.CharField(primary_key=True, max_length=10)
    first_nom = models.CharField(max_length=15)
    ape_mat = models.CharField(max_length=15)
    ape_pat = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'dat_personal'


class DetallCompra(models.Model):
    id_detall = models.IntegerField(primary_key=True)
    proces_venta_id_venta = models.ForeignKey('ProcesVenta', models.DO_NOTHING, db_column='proces_venta_id_venta')
    fecha_detall = models.DateField()
    nom_producto = models.CharField(max_length=15)
    cost_producto = models.IntegerField()
    iva_producto = models.IntegerField()
    total_compra = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detall_compra'


class DirecExtran(models.Model):
    vent_extran_id_vent_ex = models.ForeignKey('VentExtran', models.DO_NOTHING, db_column='vent_extran_id_vent_ex')
    id_direc = models.CharField(primary_key=True, max_length=20)
    pais = models.CharField(max_length=20)
    direc_cli = models.CharField(max_length=20)
    num_calle = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=10, blank=True, null=True)
    localidad = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'direc_extran'


class DirecLocal(models.Model):
    id_direc = models.CharField(primary_key=True, max_length=20)
    direc_cli = models.CharField(max_length=20)
    num_calle = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=20)
    comuna = models.CharField(max_length=20)
    vent_local_id_vent_loc = models.ForeignKey('VentLocal', models.DO_NOTHING, db_column='vent_local_id_vent_loc')

    class Meta:
        managed = False
        db_table = 'direc_local'



class ProcesVenta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        managed = False
        db_table = 'proces_venta'


class Productos(models.Model):
    id_prod = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nom_prod = models.CharField(max_length=20)
    precio_prod = models.IntegerField()
    stock_prod = models.IntegerField()
    transporte_id_trans = models.ForeignKey('Transporte', models.DO_NOTHING,blank=True, null=True, db_column='transporte_id_trans')
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        managed = False
        db_table = 'productos'


class Registro(models.Model):
    email = models.CharField(primary_key=True, max_length=20)
    dat_personal_id_dat = models.ForeignKey(DatPersonal, models.DO_NOTHING, db_column='dat_personal_id_dat')
    password = models.CharField(max_length=20)
    confir_contra = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'registro'
        unique_together = (('email', 'password'),)


class ReportMerma(models.Model):
    id_merma = models.IntegerField(primary_key=True)
    fecha_merma = models.DateField()
    descrip_merma = models.CharField(max_length=40)
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        managed = False
        db_table = 'report_merma'


class ReportVenta(models.Model):
    id_report_vent = models.IntegerField(primary_key=True)
    prod_venta = models.CharField(max_length=20)
    cant_venta = models.IntegerField()
    total_venta = models.IntegerField()
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        managed = False
        db_table = 'report_venta'


class Reportes(models.Model):
    id_report = models.IntegerField(primary_key=True)
    fecha_report = models.DateField()
    tip_report = models.CharField(max_length=15)
    user_report = models.CharField(max_length=15)
    descrip_report = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'reportes'


class SeguiProd(models.Model):
    productos_id_prod = models.ForeignKey(Productos, models.DO_NOTHING, db_column='productos_id_prod')
    est_segui = models.CharField(max_length=15)
    seguimiento_est_seguimiento = models.ForeignKey('Seguimiento', models.DO_NOTHING, db_column='seguimiento_est_seguimiento')

    class Meta:
        managed = False
        db_table = 'segui_prod'


class Seguimiento(models.Model):
    est_seguimiento = models.CharField(primary_key=True, max_length=20)
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        managed = False
        db_table = 'seguimiento'



class SubaTrans(models.Model):
    subastas_id_sub = models.ForeignKey('Subastas', models.DO_NOTHING, db_column='subastas_id_sub')
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        managed = False
        db_table = 'suba_trans'


class Subastas(models.Model):
    id_sub = models.IntegerField(primary_key=True)
    min_postor = models.IntegerField()
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        managed = False
        db_table = 'subastas'


class Transporte(models.Model):
    id_trans = models.IntegerField(primary_key=True)
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')
    tip_transporte = models.CharField(max_length=15)
    tamano_trans = models.IntegerField()
    capacidad_trans = models.IntegerField()
    refrigeracion_trans = models.CharField(max_length=10)
    subastas_id_sub = models.ForeignKey(Subastas, models.DO_NOTHING, db_column='subastas_id_sub')

    class Meta:
        managed = False
        db_table = 'transporte'


class UserReport(models.Model):
    reportes_id_report = models.ForeignKey(Reportes, models.DO_NOTHING, db_column='reportes_id_report')
    usuarios_usuarios_id_user = models.ForeignKey('UsuariosUsuarios', models.DO_NOTHING, db_column='usuarios_usuarios_id_user')

    class Meta:
        managed = False
        db_table = 'user_report'


class UsuariosUsuarios(models.Model):
    id_user = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    tipo_usuario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_usuarios'




class VentExtran(models.Model):
    id_vent_ex = models.CharField(primary_key=True, max_length=10)
    proces_venta_id_venta = models.ForeignKey(ProcesVenta, models.DO_NOTHING, db_column='proces_venta_id_venta')
    nom_cli = models.CharField(max_length=20)
    ape_pat = models.CharField(max_length=20)
    ape_mat = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'vent_extran'


class VentLocal(models.Model):
    id_vent_loc = models.CharField(primary_key=True, max_length=10)
    proces_venta_id_venta = models.ForeignKey(ProcesVenta, models.DO_NOTHING, db_column='proces_venta_id_venta')
    nom_cli = models.CharField(max_length=20)
    ape_pat = models.CharField(max_length=20)
    ape_mat = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'vent_local'
