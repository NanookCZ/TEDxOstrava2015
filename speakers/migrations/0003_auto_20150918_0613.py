# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20150917_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='talk_name',
            field=models.CharField(max_length=225, null=True, verbose_name='talk_name', blank=True),
        ),
    ]
