# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tedx', '0004_auto_20150803_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tedx',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tedx',
            name='language',
        ),
    ]
