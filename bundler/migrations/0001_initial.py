# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wizard', '0044_remove_challengemodel_is_ready'),
    ]

    operations = [
        migrations.CreateModel(
            name='BundleTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('scheduled', 'Scheduled'), ('started', 'Started'), ('cancelled', 'Cancelled'), ('finished', 'Finished')], max_length=10)),
                ('progress_perc', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('closed', models.DateTimeField(null=True)),
                ('output', models.FileField(null=True, upload_to='')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizard.ChallengeModel')),
            ],
        ),
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('level', models.IntegerField()),
                ('message', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='bundler.BundleTaskModel')),
            ],
        ),
    ]