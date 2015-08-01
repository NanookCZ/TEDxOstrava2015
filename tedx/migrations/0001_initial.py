# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('website', models.URLField(null=True, verbose_name='website', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='logo', blank=True)),
                ('language', models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True)),
            ],
            options={
                'verbose_name': 'About app',
                'verbose_name_plural': 'About app',
            },
        ),
        migrations.CreateModel(
            name='TEDx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('website', models.URLField(null=True, verbose_name='website', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('is_published', models.BooleanField(default=False)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='tedx_logo', blank=True)),
                ('event_start', models.DateField(null=True, verbose_name='event_start', blank=True)),
                ('language', models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True)),
            ],
            options={
                'verbose_name': 'TEDx',
                'verbose_name_plural': 'TEDx',
            },
        ),
    ]
