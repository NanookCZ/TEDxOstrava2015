# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0002_auto_20150801_1940'),
        ('partners', '0002_remove_partner_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
    ]
