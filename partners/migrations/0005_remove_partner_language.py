# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_auto_20150803_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='language',
        ),
    ]
