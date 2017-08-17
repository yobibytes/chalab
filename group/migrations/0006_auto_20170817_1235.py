# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_auto_20170725_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmodel',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
