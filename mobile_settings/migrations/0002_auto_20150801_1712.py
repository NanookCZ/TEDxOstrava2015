# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='language',
            field=models.ForeignKey(blank=True, to='events.Language', null=True),
        ),
    ]
