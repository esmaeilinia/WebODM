# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 17:19
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_task_available_assets'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dsm_extent',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, help_text='Extent of the DSM created by OpenDroneMap', null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='task',
            name='dtm_extent',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, help_text='Extent of the DTM created by OpenDroneMap', null=True, srid=4326),
        ),
    ]