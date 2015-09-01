# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0001_initial'),
        ('events', '0002_remove_theme_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='banner',
            field=models.ForeignKey(blank=True, to='mobile_settings.Image', null=True),
        ),
    ]
