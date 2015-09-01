# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='image',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='language',
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_logo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
    ]
