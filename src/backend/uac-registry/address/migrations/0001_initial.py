# Generated by Django 3.1.3 on 2020-12-04 06:07

import django.core.validators
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('number', models.PositiveIntegerField(blank=True)),
                ('additional_info', models.CharField(blank=True, max_length=100)),
                ('postal_code', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='The postal code must be in the format 01234567', regex='^[0-9]{8}$')])),
                ('public_place', models.CharField(choices=[('AER', 'Aeroporto'), ('AL', 'Alameda'), ('AV', 'Avenida'), ('BC', 'Beco'), ('BL', 'Bloco'), ('BO', 'Bosque'), ('CAM', 'Caminho'), ('ESC', 'Escadinha'), ('ETC', 'Estação'), ('EST', 'Estrada'), ('FAZ', 'Fazenda'), ('FER', 'Ferrovia'), ('GLR', 'Galeria'), ('LAD', 'Ladeira'), ('LGO', 'Largo'), ('LIM', 'Limite'), ('LINHA', 'Linha de Transmissão'), ('MANG', 'Mangue'), ('MAR', 'Margem'), ('MT', 'Monte'), ('MRO', 'Morro'), ('PQ', 'Parque'), ('PCA', 'Praça'), ('PR', 'Praia'), ('PRL', 'Prologamento'), ('PAS', 'Passagem'), ('RODOVIA', 'Rodovia'), ('R', 'Rua'), ('SQD', 'Superquadra'), ('TR', 'Travessa'), ('VD', 'Viaduto'), ('VL', 'Vila')], max_length=7)),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('PA', 'Pará'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('TO', 'Tocantins'), ('AL', 'Alagoas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('MA', 'Maranhão'), ('RN', 'Rio Grande do Norte'), ('SE', 'Sergipe'), ('ES', 'Espírito Santo'), ('MG', 'Minas Gerais'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('DF', 'Distrito Federal'), ('GO', 'Goiás'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PR', 'Paraná'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina')], max_length=2)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
