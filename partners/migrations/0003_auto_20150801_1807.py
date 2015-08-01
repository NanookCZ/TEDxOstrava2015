# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20150801_0555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Partner', 'verbose_name_plural': 'Partners'},
        ),
        migrations.RemoveField(
            model_name='partner',
            name='partner_logo',
        ),
        migrations.AddField(
            model_name='partner',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='partner_logo', blank=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_website',
            field=models.URLField(null=True, verbose_name='partner_website', blank=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
    ]
