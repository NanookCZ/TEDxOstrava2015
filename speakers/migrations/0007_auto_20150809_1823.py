# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0006_auto_20150803_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='share_message',
            field=models.CharField(default='Share...', max_length=25, verbose_name='share_message'),
        ),
    ]
