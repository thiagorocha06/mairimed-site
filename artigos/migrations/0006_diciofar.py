# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0005_diciomed'),
    ]

    operations = [
        migrations.CreateModel(
            name='DicioFar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('classe', models.CharField(max_length=50)),
                ('subclasse', models.CharField(max_length=50)),
                ('marcas', models.CharField(max_length=50)),
                ('farmacodinamica', models.CharField(max_length=50)),
                ('farmacocinetica', models.CharField(max_length=50)),
                ('absorcao', models.CharField(max_length=50)),
                ('distribuicao', models.CharField(max_length=50)),
                ('metabolismo', models.CharField(max_length=50)),
                ('eliminacao', models.CharField(max_length=50)),
                ('indicacoes', models.CharField(max_length=50)),
                ('posologia', models.CharField(max_length=50)),
                ('pediatria', models.CharField(max_length=50)),
                ('administracao', models.CharField(max_length=50)),
                ('rmuitocomum', models.CharField(max_length=50)),
                ('rcomum', models.CharField(max_length=50)),
                ('rincomum', models.CharField(max_length=50)),
                ('rrara', models.CharField(max_length=50)),
                ('rmuitorara', models.CharField(max_length=50)),
                ('rnaodefinida', models.CharField(max_length=50)),
                ('alteracaoexames', models.CharField(max_length=50)),
                ('contraindicacoes', models.CharField(max_length=50)),
                ('gravidez', models.CharField(max_length=50)),
                ('lactacao', models.CharField(max_length=50)),
            ],
        ),
    ]