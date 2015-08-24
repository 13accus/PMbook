# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0002_auto_20150819_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.DecimalField(max_digits=6, decimal_places=3)),
                ('active', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
