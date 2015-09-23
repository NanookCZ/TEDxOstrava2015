# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_auto_20150923_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True),
        ),
    ]
