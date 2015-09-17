# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tedx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tedx',
            name='title',
            field=models.CharField(max_length=150, verbose_name='title'),
        ),
    ]
