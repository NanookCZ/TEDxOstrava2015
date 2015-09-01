# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0008_speaker_speaker_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='speaker_url',
        ),
        migrations.AlterField(
            model_name='speaker',
            name='speaker_photo',
            field=models.ForeignKey(blank=True, to='mobile_settings.Image', null=True),
        ),
    ]
