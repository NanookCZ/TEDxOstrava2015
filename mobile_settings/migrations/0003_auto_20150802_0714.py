# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0002_auto_20150802_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.CharField(default='English', max_length=50, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='menu',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
    ]
