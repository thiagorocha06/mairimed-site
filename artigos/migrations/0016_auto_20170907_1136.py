# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-07 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0015_artigo_referencias'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='modulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]