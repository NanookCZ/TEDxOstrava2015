# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0007_auto_20150809_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='speaker_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
