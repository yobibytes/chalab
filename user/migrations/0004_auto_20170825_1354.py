# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-25 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170817_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='actual_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.GroupModel'),
        ),
    ]
