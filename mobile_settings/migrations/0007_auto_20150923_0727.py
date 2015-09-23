# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0006_mpnsdevice'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(default='EN', max_length=5, verbose_name='code'),
        ),
    ]
