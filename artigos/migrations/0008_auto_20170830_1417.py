# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-30 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0007_categoriasartigos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoriasArtigos',
        ),
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
