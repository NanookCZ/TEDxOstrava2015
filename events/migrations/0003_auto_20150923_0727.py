# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150917_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True, verbose_name='Language'),
        ),
    ]
