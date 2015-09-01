# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150901_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='banner',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
    ]
