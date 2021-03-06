# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0004_auto_20150905_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
    ]
