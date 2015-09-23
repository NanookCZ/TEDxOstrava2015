# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0003_auto_20150918_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True, verbose_name='Language'),
        ),
    ]
