# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0005_auto_20150901_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title_en',
            field=models.CharField(max_length=55, null=True, verbose_name='title_en', blank=True),
        ),
    ]
