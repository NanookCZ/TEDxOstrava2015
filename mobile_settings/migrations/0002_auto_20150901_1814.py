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
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True)),
                ('round_image', models.URLField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.RemoveField(
            model_name='menu',
            name='language',
        ),
        migrations.AddField(
            model_name='menu',
            name='title_en',
            field=models.CharField(max_length=55, null=True, verbose_name='title_en', blank=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='unique_key',
            field=models.SlugField(unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(default='English', max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=55, null=True, verbose_name='title', blank=True),
        ),
    ]
