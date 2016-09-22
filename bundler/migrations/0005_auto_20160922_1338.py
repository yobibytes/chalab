# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-22 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import wizard.models


class Migration(migrations.Migration):

    dependencies = [
        ('bundler', '0004_auto_20160914_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundletaskmodel',
            name='output',
            field=models.FileField(null=True, upload_to=wizard.models.StorageNameFactory('data', 'bundles')),
        ),
    ]
