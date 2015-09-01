# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0006_auto_20150901_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True)),
                ('round_image', models.URLField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
