# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='cpu_load',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stat',
            name='network_speed',
            field=models.IntegerField(),
        ),
    ]
