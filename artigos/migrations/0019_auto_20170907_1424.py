# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-07 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0018_auto_20170907_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='clas_figura',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='classificacao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='diag_figura',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='epidemio_figura',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_figura',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_texto1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_texto2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_texto3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_texto4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_top1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_top2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_top3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_top4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='exames_texto1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='exames_texto2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='exames_texto3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='exames_texto4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='exames_top1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='exames_top2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='exames_top3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='exames_top4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_texto1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_texto2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_texto3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_texto4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_top1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_top2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_top3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='med_top4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='prof_figura',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='trat_figura',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='algoritmo',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='intro_figura',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]