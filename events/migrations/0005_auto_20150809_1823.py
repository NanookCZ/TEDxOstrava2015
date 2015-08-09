# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150803_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='share_message',
            field=models.CharField(default='Share...', max_length=50, verbose_name='share_message'),
        ),
    ]
