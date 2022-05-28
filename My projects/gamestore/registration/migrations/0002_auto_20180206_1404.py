# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]