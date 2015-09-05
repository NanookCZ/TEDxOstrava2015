# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0001_initial'),
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='speaker_photo',
            field=models.ForeignKey(blank=True, to='mobile_settings.Image', null=True),
        ),
    ]
