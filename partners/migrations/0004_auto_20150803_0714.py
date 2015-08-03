# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20150802_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='image',
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_logo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
    ]
