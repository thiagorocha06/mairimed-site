# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigo',
            name='favoritos',
        ),
    ]