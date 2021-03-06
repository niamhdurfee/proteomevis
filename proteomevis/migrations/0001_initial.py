# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-11 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain_id', models.IntegerField(default=0)),
                ('species', models.IntegerField(default=0)),
                ('pdb', models.CharField(max_length=10)),
                ('domain', models.CharField(max_length=10)),
                ('chain', models.CharField(max_length=2)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('abundance', models.IntegerField(blank=True, null=True)),
                ('evorate', models.FloatField(blank=True, null=True)),
                ('conden', models.FloatField(blank=True, null=True)),
                ('dostox', models.FloatField(blank=True, null=True)),
                ('dN', models.FloatField(blank=True, null=True)),
                ('dS', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('domain', models.CharField(blank=True, max_length=10, null=True)),
                ('uniprot', models.CharField(blank=True, max_length=30, null=True)),
                ('genes', models.CharField(blank=True, max_length=30, null=True)),
                ('details', models.CharField(blank=True, max_length=200, null=True)),
                ('function1', models.CharField(blank=True, max_length=200, null=True)),
                ('function2', models.CharField(blank=True, max_length=30, null=True)),
                ('invis', models.BooleanField()),
                ('obsolete', models.CharField(blank=True, max_length=30, null=True)),
                ('species', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DomainLocalization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniprot', models.CharField(max_length=10)),
                ('localizationID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceID', models.IntegerField(default=0)),
                ('species', models.IntegerField(default=0)),
                ('targetID', models.IntegerField(default=0)),
                ('sid', models.FloatField(blank=True, null=True)),
                ('tm', models.FloatField(blank=True, null=True)),
                ('ppi', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('function', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('localization', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('has_localization', models.BooleanField()),
                ('has_function', models.BooleanField()),
            ],
        ),
    ]
