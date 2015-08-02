# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_remove_speaker_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='speaker_photo', blank=True),
        ),
    ]
