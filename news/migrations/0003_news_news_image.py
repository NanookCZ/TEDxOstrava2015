# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.ForeignKey(blank=True, to='mobile_settings.Image', null=True),
        ),
    ]
