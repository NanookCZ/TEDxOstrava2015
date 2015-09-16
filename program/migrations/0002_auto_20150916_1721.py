# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0006_mpnsdevice'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='language',
            field=models.ForeignKey(blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='language',
            field=models.ForeignKey(blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='language',
            field=models.ForeignKey(blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='language',
            field=models.ForeignKey(blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AddField(
            model_name='slotkind',
            name='language',
            field=models.ForeignKey(blank=True, to='mobile_settings.Language', null=True),
        ),
    ]
