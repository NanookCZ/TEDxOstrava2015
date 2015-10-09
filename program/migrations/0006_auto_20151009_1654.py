# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_auto_20151009_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='slot',
            field=models.ForeignKey(blank=True, to='program.Slot', null=True),
        ),
    ]
