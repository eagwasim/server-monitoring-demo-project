# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(max_length=1024)),
                ('uri', models.CharField(max_length=1024)),
                ('status', models.CharField(max_length=1024)),
                ('type', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='ServerSpec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ram', models.IntegerField()),
                ('disk_size', models.IntegerField()),
                ('processor', models.CharField(default=b'', max_length=1024)),
                ('server', models.ForeignKey(to='monitor.Server')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('network_speed', models.DecimalField(max_digits=9999999999, decimal_places=2)),
                ('cpu_load', models.DecimalField(max_digits=9999999999, decimal_places=2)),
                ('cpu_usage', models.IntegerField()),
                ('free_ram', models.IntegerField()),
                ('server', models.ForeignKey(to='monitor.Server')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=1024)),
                ('password', models.CharField(max_length=1024)),
            ],
        ),
    ]
