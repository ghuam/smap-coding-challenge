# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-16 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumption',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consumption.User'),
        ),
    ]