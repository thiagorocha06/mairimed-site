# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-12 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0030_auto_20170912_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='med_texto5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_texto6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_top5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_top6',
            field=models.TextField(blank=True, null=True),
        ),
    ]
