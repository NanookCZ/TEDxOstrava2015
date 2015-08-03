# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('tedx', '0003_auto_20150802_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutapp',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tedx',
            name='image',
        ),
        migrations.AddField(
            model_name='aboutapp',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
        migrations.AddField(
            model_name='tedx',
            name='tedx_logo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
    ]
