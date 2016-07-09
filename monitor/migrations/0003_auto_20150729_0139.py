# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20150728_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='disk_size',
            field=models.IntegerField(default=datetime.datetime(2015, 7, 29, 1, 39, 43, 171972, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='processor',
            field=models.CharField(default=b'', max_length=1024),
        ),
        migrations.AddField(
            model_name='server',
            name='ram',
            field=models.IntegerField(default=datetime.datetime(2015, 7, 29, 1, 39, 48, 251529, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
