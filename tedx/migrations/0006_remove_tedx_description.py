# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tedx', '0005_remove_tedx_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tedx',
            name='description',
        ),
    ]
