# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezerwacje', '0004_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokoj',
            name='mapcoords',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokoj',
            name='maphref',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokoj',
            name='mapshape',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
