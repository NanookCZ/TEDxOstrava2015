# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0006_auto_20150901_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='speaker_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='speaker_photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
    ]
