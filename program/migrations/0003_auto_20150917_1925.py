# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20150916_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(help_text='Section name, i.e. TEDx Talk, Worskhops,...', max_length=100),
        ),
        migrations.AlterField(
            model_name='slotkind',
            name='slot_name',
            field=models.CharField(help_text='Sloat name - i. e. Talk, Lunch, Break, ..', max_length=150),
        ),
    ]
