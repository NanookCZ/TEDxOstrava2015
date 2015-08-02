# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0003_auto_20150802_0714'),
        ('partners', '0002_remove_partner_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
    ]
