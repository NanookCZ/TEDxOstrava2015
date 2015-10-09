# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0007_auto_20150923_0727'),
        ('program', '0004_auto_20150923_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='section',
        ),
        migrations.AddField(
            model_name='presentation',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='cover_image',
            field=models.ForeignKey(blank=True, to='mobile_settings.Image', null=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='end',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='start',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='presentation',
            name='ted_talk_video',
            field=models.URLField(null=True, blank=True),
        ),
    ]
