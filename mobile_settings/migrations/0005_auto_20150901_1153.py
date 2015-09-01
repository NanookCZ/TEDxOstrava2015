# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0004_menu_unique_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='language',
        ),
        migrations.AddField(
            model_name='menu',
            name='title_en',
            field=models.CharField(max_length=55, null=True, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=55, null=True, verbose_name='title', blank=True),
        ),
    ]
