# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150901_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='banner',
            field=models.ForeignKey(verbose_name='Image', blank=True, to='mobile_settings.Image', null=True),
        ),
    ]
