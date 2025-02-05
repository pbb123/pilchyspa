# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezerwacje', '0005_auto_20170923_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer', models.IntegerField()),
                ('limit', models.IntegerField()),
                ('nazwa', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='rezerwacja',
            name='rozmiar',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
