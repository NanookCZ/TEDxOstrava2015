# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150801_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='language',
            field=models.ForeignKey(blank=True, to='events.Language', null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='language',
            field=models.ForeignKey(blank=True, to='events.Language', null=True),
        ),
    ]
