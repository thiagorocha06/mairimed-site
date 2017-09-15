# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-15 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmaco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, max_length=50, null=True)),
                ('classe', models.TextField(blank=True, null=True)),
                ('subclasse', models.TextField(blank=True, null=True)),
                ('marcas', models.TextField(blank=True, null=True)),
                ('farmacodinamica', models.TextField(blank=True, null=True)),
                ('farmacocinetica', models.TextField(blank=True, null=True)),
                ('absorcao', models.TextField(blank=True, null=True)),
                ('distribuicao', models.TextField(blank=True, null=True)),
                ('metabolismo', models.TextField(blank=True, null=True)),
                ('eliminacao', models.TextField(blank=True, null=True)),
                ('indicacoes', models.TextField(blank=True, null=True)),
                ('posologia', models.TextField(blank=True, null=True)),
                ('pediatria', models.TextField(blank=True, null=True)),
                ('administracao', models.TextField(blank=True, null=True)),
                ('rmuitocomum', models.TextField(blank=True, null=True)),
                ('rcomum', models.TextField(blank=True, null=True)),
                ('rincomum', models.TextField(blank=True, null=True)),
                ('rrara', models.TextField(blank=True, null=True)),
                ('rmuitorara', models.TextField(blank=True, null=True)),
                ('rnaodefinida', models.TextField(blank=True, null=True)),
                ('alteracaoexames', models.TextField(blank=True, null=True)),
                ('contraindicacoes', models.TextField(blank=True, null=True)),
                ('gravidez', models.TextField(blank=True, null=True)),
                ('lactacao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
