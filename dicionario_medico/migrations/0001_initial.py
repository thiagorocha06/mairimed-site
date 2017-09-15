# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-15 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Termo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('origem', models.TextField(blank=True, max_length=50, null=True)),
                ('definicao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]