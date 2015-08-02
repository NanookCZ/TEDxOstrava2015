# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0003_auto_20150802_0714'),
        ('news', '0002_auto_20150802_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
    ]
