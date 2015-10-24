# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0007_auto_20150923_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mpnsdevice',
            name='user',
        ),
        migrations.AlterField(
            model_name='image',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_title',
            field=models.CharField(max_length=55, null=True, verbose_name='image_title', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='round_image',
            field=models.URLField(null=True, verbose_name='round_image', blank=True),
        ),
        migrations.DeleteModel(
            name='MPNSDevice',
        ),
    ]
