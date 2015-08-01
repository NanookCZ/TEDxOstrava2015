# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150801_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='language',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='language',
        ),
    ]
