# Generated by Django 3.1.1 on 2020-10-05 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id_contrat', models.IntegerField(primary_key=True, serialize=False)),
                ('emision_contrat', models.DateField()),
                ('fin_contrat', models.DateField()),
            ],
            options={
                'db_table': 'contratos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContratPerson',
            fields=[
                ('rut_person', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_contrat', models.CharField(max_length=20)),
                ('phone_contrat', models.IntegerField()),
            ],
            options={
                'db_table': 'contrat_person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_prod_pedido', models.CharField(max_length=20)),
                ('cant_prod', models.IntegerField()),
            ],
            options={
                'db_table': 'pedido',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='DatPersonal',
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
        migrations.DeleteModel(
            name='UserReport',
        ),
    ]