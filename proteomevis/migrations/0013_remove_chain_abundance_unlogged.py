# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proteomevis', '0012_species_has_mutant_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chain',
            name='abundance_unlogged',
        ),
    ]
