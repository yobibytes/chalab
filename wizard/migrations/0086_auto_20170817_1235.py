# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 12:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0085_auto_20170727_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengemodel',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='organization_name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='origin_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.GroupModel'),
        ),
        migrations.AlterField(
            model_name='datasetmodel',
            name='authors',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='datasetmodel',
            name='default_metric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wizard.MetricModel'),
        ),
        migrations.AlterField(
            model_name='datasetmodel',
            name='keywords',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='datasetmodel',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='metricmodel',
            name='code',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='metricmodel',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='metricmodel',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
