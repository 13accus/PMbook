# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='capnum',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='cap',
            field=models.CharField(max_length=1000),
        ),
    ]
