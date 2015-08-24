# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(default=1)),
                ('capability', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('division', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('health', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('initiative', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default=b'No Title', max_length=100)),
                ('comment', models.CharField(max_length=10000)),
                ('resolved', models.BooleanField(default=True)),
                ('project_id', models.IntegerField()),
                ('open_date', models.DateField(default=datetime.datetime.now)),
                ('close_date', models.DateField(default=datetime.datetime.now)),
                ('next_step', models.CharField(default=b'', max_length=10000)),
                ('assign_to', models.CharField(default=b'', max_length=1000)),
                ('external_dependencies', models.CharField(default=b'', max_length=10000)),
                ('issue_id', models.IntegerField(default=0)),
                ('newest', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Methodology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('methodology', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('comment', models.CharField(max_length=10000)),
                ('project_id', models.IntegerField()),
                ('mile_type', models.CharField(default=b'', max_length=100)),
                ('baseline_date', models.DateField()),
                ('target_date', models.DateField()),
                ('milestone_id', models.IntegerField()),
                ('newest', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('comment', models.CharField(max_length=10000)),
                ('project_id', models.IntegerField()),
                ('note_id', models.IntegerField()),
                ('newest', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('project_id', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('sponsor', models.CharField(max_length=100)),
                ('poc', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('launchdate', models.DateField(default=datetime.datetime.now)),
                ('staff', models.CharField(default=b'', max_length=10000)),
                ('v1', models.CharField(default=b'', max_length=10000)),
                ('v2', models.CharField(default=b'', max_length=10000)),
                ('v3', models.CharField(default=b'', max_length=10000)),
                ('v4', models.CharField(default=b'', max_length=10000)),
                ('v5', models.CharField(default=b'', max_length=10000)),
                ('comment', models.CharField(default=b'', max_length=10000)),
                ('needyn1', models.CharField(default=b'', max_length=10000)),
                ('needyn2', models.CharField(default=b'', max_length=10000)),
                ('needyn3', models.CharField(default=b'', max_length=10000)),
                ('needyn4', models.CharField(default=b'', max_length=10000)),
                ('needyn5', models.CharField(default=b'', max_length=10000)),
                ('needyn6', models.CharField(default=b'', max_length=10000)),
                ('valueyn1', models.CharField(default=b'', max_length=10000)),
                ('valueyn2', models.CharField(default=b'', max_length=10000)),
                ('valueyn3', models.CharField(default=b'', max_length=10000)),
                ('valueyn4', models.CharField(default=b'', max_length=10000)),
                ('valueyn5', models.CharField(default=b'', max_length=10000)),
                ('valueyn6', models.CharField(default=b'', max_length=10000)),
                ('techrisk1', models.CharField(default=b'', max_length=10000)),
                ('techrisk2', models.CharField(default=b'', max_length=10000)),
                ('techrisk3', models.CharField(default=b'', max_length=10000)),
                ('techrisk4', models.CharField(default=b'', max_length=10000)),
                ('techrisk5', models.CharField(default=b'', max_length=10000)),
                ('techrisk6', models.CharField(default=b'', max_length=10000)),
                ('techrisk7', models.CharField(default=b'', max_length=10000)),
                ('poc_contact_info', models.CharField(max_length=100)),
                ('project_id', models.IntegerField()),
                ('cap', models.ForeignKey(default=b'', to='Models.Capability')),
                ('division', models.ForeignKey(to='Models.Division')),
                ('method', models.ForeignKey(default=1, to='Models.Methodology')),
                ('office', models.ForeignKey(to='Models.Office')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue', models.ForeignKey(to='Models.Issue')),
                ('milestone', models.ForeignKey(to='Models.Milestone')),
                ('note', models.ForeignKey(to='Models.Note')),
                ('project', models.ForeignKey(to='Models.Project')),
            ],
        ),
        migrations.CreateModel(
            name='RI_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ri_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('comment', models.CharField(max_length=10000)),
                ('resolved', models.BooleanField(default=True)),
                ('project_id', models.IntegerField()),
                ('open_date', models.DateField(default=datetime.datetime.now)),
                ('close_date', models.DateField()),
                ('next_step', models.CharField(max_length=10000)),
                ('assigned_to', models.CharField(max_length=100)),
                ('external_dependencies', models.CharField(max_length=1000)),
                ('risk_id', models.IntegerField()),
                ('newest', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='Models.RI_Category')),
                ('probability', models.ForeignKey(to='Models.Level')),
                ('severity', models.ForeignKey(to='Models.Health')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('milestone_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='projectpackage',
            name='risk',
            field=models.ForeignKey(to='Models.Risk'),
        ),
        migrations.AddField(
            model_name='projectpackage',
            name='roles',
            field=models.ForeignKey(to='Models.Personnel'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default=1, to='Models.Status'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='role',
            field=models.ForeignKey(default=b'', to='Models.Role'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='status',
            field=models.ForeignKey(to='Models.Status'),
        ),
        migrations.AddField(
            model_name='issue',
            name='category',
            field=models.ForeignKey(default=b'', to='Models.RI_Category'),
        ),
        migrations.AddField(
            model_name='issue',
            name='severity',
            field=models.ForeignKey(to='Models.Health'),
        ),
    ]
