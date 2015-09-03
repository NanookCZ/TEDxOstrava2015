# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_title',
            field=models.CharField(max_length=55, null=True, verbose_name='title', blank=True),
        ),
    ]
