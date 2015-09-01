# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150901_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
    ]
