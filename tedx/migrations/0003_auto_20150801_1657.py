# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150801_1657'),
        ('tedx', '0002_auto_20150801_0555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutapp',
            options={'verbose_name': 'About app', 'verbose_name_plural': 'About app'},
        ),
        migrations.AlterModelOptions(
            name='tedx',
            options={'verbose_name': 'TEDx', 'verbose_name_plural': 'TEDx'},
        ),
        migrations.RemoveField(
            model_name='aboutapp',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='tedx',
            name='tedx_logo',
        ),
        migrations.AddField(
            model_name='aboutapp',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='logo', blank=True),
        ),
        migrations.AddField(
            model_name='aboutapp',
            name='language',
            field=models.ForeignKey(to_field='language', blank=True, to='events.Language', null=True),
        ),
        migrations.AddField(
            model_name='tedx',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='tedx_logo', blank=True),
        ),
        migrations.AddField(
            model_name='tedx',
            name='language',
            field=models.ForeignKey(to_field='language', blank=True, to='events.Language', null=True),
        ),
        migrations.AlterField(
            model_name='aboutapp',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='aboutapp',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='aboutapp',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aboutapp',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='aboutapp',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
        migrations.AlterField(
            model_name='aboutapp',
            name='website',
            field=models.URLField(null=True, verbose_name='website', blank=True),
        ),
        migrations.AlterField(
            model_name='tedx',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='tedx',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='tedx',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='tedx',
            name='event_start',
            field=models.DateField(null=True, verbose_name='event_start', blank=True),
        ),
        migrations.AlterField(
            model_name='tedx',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='tedx',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
        migrations.AlterField(
            model_name='tedx',
            name='website',
            field=models.URLField(null=True, verbose_name='website', blank=True),
        ),
    ]
