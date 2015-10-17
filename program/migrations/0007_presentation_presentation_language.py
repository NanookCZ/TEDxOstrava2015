# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_auto_20151009_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='presentation_language',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
