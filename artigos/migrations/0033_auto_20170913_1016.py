# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-13 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0032_auto_20170912_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artigo',
            old_name='etio_figura',
            new_name='etio_img1',
        ),
        migrations.AddField(
            model_name='artigo',
            name='etio_img2',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]