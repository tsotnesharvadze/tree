# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personmodel',
            name='children',
        ),
        migrations.AddField(
            model_name='personmodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_set', to='hierarchy.PersonModel', verbose_name='მშობელი'),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='sex',
            field=models.CharField(choices=[('0', 'ქალი'), ('1', 'კაცი')], max_length=1, verbose_name='სქესი'),
        ),
    ]
