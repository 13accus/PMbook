# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0003_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='RIdeck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cap', models.IntegerField()),
                ('proj_id', models.IntegerField()),
                ('proj_name', models.CharField(max_length=100)),
                ('bus_own', models.CharField(max_length=100)),
                ('tar_date', models.DateField()),
                ('status1', models.CharField(max_length=100)),
                ('status2', models.CharField(max_length=100)),
                ('status3', models.CharField(max_length=100)),
                ('close_date', models.DateField()),
                ('key_dependencies', models.CharField(max_length=10000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='projectpackage',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='projectpackage',
            name='milestone',
        ),
        migrations.RemoveField(
            model_name='projectpackage',
            name='note',
        ),
        migrations.RemoveField(
            model_name='projectpackage',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectpackage',
            name='risk',
        ),
        migrations.RemoveField(
            model_name='projectpackage',
            name='roles',
        ),
        migrations.DeleteModel(
            name='ProjectPackage',
        ),
    ]
