# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '__first__'),
        ('speakers', '0003_auto_20150801_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
    ]
