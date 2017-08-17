# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_auto_20170817_1235'),
        ('user', '0002_auto_20160902_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='actual_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='group.GroupModel'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='expertise',
            field=models.CharField(choices=[('NO', 'Novice'), ('FA', 'Familiar'), ('EX', 'Expert')], default='NO', max_length=2),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]