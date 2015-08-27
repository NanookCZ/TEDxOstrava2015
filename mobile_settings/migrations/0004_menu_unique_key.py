# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0003_auto_20150802_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='unique_key',
            field=models.SlugField(unique=True, null=True, blank=True),
        ),
    ]
