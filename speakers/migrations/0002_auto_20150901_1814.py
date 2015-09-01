# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0002_auto_20150901_1814'),
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='image',
        ),
        migrations.AddField(
            model_name='speaker',
            name='speaker_photo',
            field=models.ForeignKey(blank=True, to='mobile_settings.Image', null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='share_message',
            field=models.CharField(default='Share...', max_length=25, verbose_name='share_message'),
        ),
    ]
